# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

function Set-ScriptExtent {
    <#
    .EXTERNALHELP ..\PowerShellEditorServices.Commands-help.xml
    #>
    [CmdletBinding(PositionalBinding=$false, DefaultParameterSetName='__AllParameterSets')]
    param(
        [Parameter(Position=0, Mandatory)]
        [psobject]
        $Text,

        [Parameter(Mandatory, ParameterSetName='AsString')]
        [switch]
        $AsString,

        [Parameter(Mandatory, ParameterSetName='AsArray')]
        [switch]
        $AsArray,

        [Parameter(ValueFromPipeline, ValueFromPipelineByPropertyName)]
        [System.Management.Automation.Language.IScriptExtent]
        $Extent = (Find-Ast -AtCursor).Extent
    )
    begin {
        $fileContext = $psEditor.GetEditorContext().CurrentFile
        $extentList = [System.Collections.Generic.List[Microsoft.PowerShell.EditorServices.Extensions.FileScriptExtent, Microsoft.PowerShell.EditorServices]]::new()
    }
    process {
        if ($Extent -isnot [Microsoft.PowerShell.EditorServices.Extensions.FileScriptExtent, Microsoft.PowerShell.EditorServices]) {
            $Extent = [Microsoft.PowerShell.EditorServices.Extensions.FileScriptExtent, Microsoft.PowerShell.EditorServices]::FromOffsets(
                $fileContext,
                $Extent.StartOffset,
                $Extent.EndOffset)
        }
        $extentList.Add($Extent)
    }
    # Currently this kills the pipeline because we need to keep track and edit all extents for position tracking.
    # TODO: Consider queueing changes in a static property and adding a PassThru switch.
    end {
        switch ($PSCmdlet.ParameterSetName) {
            # Insert text as a single string expression.
            AsString {
                $Text = "'{0}'" -f $Text.Replace("'", "''")
            }
            # Create a string expression for each line, separated by a comma.
            AsArray {
                $newLine = [Environment]::NewLine
                $Text = "'" + ($Text.Replace("'", "''") -split '\r?\n' -join "',$newLine'") + "'"

                if ($Text.Split("`n", [StringSplitOptions]::RemoveEmptyEntries).Count -gt 1) {
                    $needsIndentFix = $true
                }
            }
        }

        foreach ($aExtent in $extentList) {
            $aText = $Text

            if ($needsIndentFix) {
                # I'd rather let PSSA handle this when there are more formatting options.
                $indentOffset = ' ' * ($aExtent.StartColumnNumber - 1)
                $aText = $aText -split '\r?\n' `
                                -join ([Environment]::NewLine + $indentOffset)
            }
            $differenceOffset = $aText.Length - $aExtent.Text.Length
            $scriptText       = $fileContext.GetText()

            $fileContext.InsertText($aText, $aExtent)

            $newText = $scriptText.Remove($aExtent.StartOffset, $aExtent.Text.Length).Insert($aExtent.StartOffset, $aText)

            $timeoutLoop = 0
            while ($fileContext.GetText() -ne $newText) {
                Start-Sleep -Milliseconds 30
                $timeoutLoop++

                if ($timeoutLoop -gt 20) {
                    $PSCmdlet.WriteDebug(('Timed out waiting for change at range {0}, {1}' -f $aExtent.StartOffset,
                                                                                              $aExtent.EndOffset))
                    break
                }
            }

            if ($differenceOffset) {
                $extentList.ForEach({
                    if ($args[0].StartOffset -ge $aExtent.EndOffset) {
                        $args[0].AddOffset($differenceOffset)
                    }
                })
            }
        }
    }
}

# SIG # Begin signature block
# MIInrQYJKoZIhvcNAQcCoIInnjCCJ5oCAQExDzANBglghkgBZQMEAgEFADB5Bgor
# BgEEAYI3AgEEoGswaTA0BgorBgEEAYI3AgEeMCYCAwEAAAQQH8w7YFlLCE63JNLG
# KX7zUQIBAAIBAAIBAAIBAAIBADAxMA0GCWCGSAFlAwQCAQUABCDjfgMwZO8HuBYC
# 7m64mbWlT7CiPdZIkRwS5bpsGFVczqCCDYEwggX/MIID56ADAgECAhMzAAACUosz
# qviV8znbAAAAAAJSMA0GCSqGSIb3DQEBCwUAMH4xCzAJBgNVBAYTAlVTMRMwEQYD
# VQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQHEwdSZWRtb25kMR4wHAYDVQQKExVNaWNy
# b3NvZnQgQ29ycG9yYXRpb24xKDAmBgNVBAMTH01pY3Jvc29mdCBDb2RlIFNpZ25p
# bmcgUENBIDIwMTEwHhcNMjEwOTAyMTgzMjU5WhcNMjIwOTAxMTgzMjU5WjB0MQsw
# CQYDVQQGEwJVUzETMBEGA1UECBMKV2FzaGluZ3RvbjEQMA4GA1UEBxMHUmVkbW9u
# ZDEeMBwGA1UEChMVTWljcm9zb2Z0IENvcnBvcmF0aW9uMR4wHAYDVQQDExVNaWNy
# b3NvZnQgQ29ycG9yYXRpb24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB
# AQDQ5M+Ps/X7BNuv5B/0I6uoDwj0NJOo1KrVQqO7ggRXccklyTrWL4xMShjIou2I
# sbYnF67wXzVAq5Om4oe+LfzSDOzjcb6ms00gBo0OQaqwQ1BijyJ7NvDf80I1fW9O
# L76Kt0Wpc2zrGhzcHdb7upPrvxvSNNUvxK3sgw7YTt31410vpEp8yfBEl/hd8ZzA
# v47DCgJ5j1zm295s1RVZHNp6MoiQFVOECm4AwK2l28i+YER1JO4IplTH44uvzX9o
# RnJHaMvWzZEpozPy4jNO2DDqbcNs4zh7AWMhE1PWFVA+CHI/En5nASvCvLmuR/t8
# q4bc8XR8QIZJQSp+2U6m2ldNAgMBAAGjggF+MIIBejAfBgNVHSUEGDAWBgorBgEE
# AYI3TAgBBggrBgEFBQcDAzAdBgNVHQ4EFgQUNZJaEUGL2Guwt7ZOAu4efEYXedEw
# UAYDVR0RBEkwR6RFMEMxKTAnBgNVBAsTIE1pY3Jvc29mdCBPcGVyYXRpb25zIFB1
# ZXJ0byBSaWNvMRYwFAYDVQQFEw0yMzAwMTIrNDY3NTk3MB8GA1UdIwQYMBaAFEhu
# ZOVQBdOCqhc3NyK1bajKdQKVMFQGA1UdHwRNMEswSaBHoEWGQ2h0dHA6Ly93d3cu
# bWljcm9zb2Z0LmNvbS9wa2lvcHMvY3JsL01pY0NvZFNpZ1BDQTIwMTFfMjAxMS0w
# Ny0wOC5jcmwwYQYIKwYBBQUHAQEEVTBTMFEGCCsGAQUFBzAChkVodHRwOi8vd3d3
# Lm1pY3Jvc29mdC5jb20vcGtpb3BzL2NlcnRzL01pY0NvZFNpZ1BDQTIwMTFfMjAx
# MS0wNy0wOC5jcnQwDAYDVR0TAQH/BAIwADANBgkqhkiG9w0BAQsFAAOCAgEAFkk3
# uSxkTEBh1NtAl7BivIEsAWdgX1qZ+EdZMYbQKasY6IhSLXRMxF1B3OKdR9K/kccp
# kvNcGl8D7YyYS4mhCUMBR+VLrg3f8PUj38A9V5aiY2/Jok7WZFOAmjPRNNGnyeg7
# l0lTiThFqE+2aOs6+heegqAdelGgNJKRHLWRuhGKuLIw5lkgx9Ky+QvZrn/Ddi8u
# TIgWKp+MGG8xY6PBvvjgt9jQShlnPrZ3UY8Bvwy6rynhXBaV0V0TTL0gEx7eh/K1
# o8Miaru6s/7FyqOLeUS4vTHh9TgBL5DtxCYurXbSBVtL1Fj44+Od/6cmC9mmvrti
# yG709Y3Rd3YdJj2f3GJq7Y7KdWq0QYhatKhBeg4fxjhg0yut2g6aM1mxjNPrE48z
# 6HWCNGu9gMK5ZudldRw4a45Z06Aoktof0CqOyTErvq0YjoE4Xpa0+87T/PVUXNqf
# 7Y+qSU7+9LtLQuMYR4w3cSPjuNusvLf9gBnch5RqM7kaDtYWDgLyB42EfsxeMqwK
# WwA+TVi0HrWRqfSx2olbE56hJcEkMjOSKz3sRuupFCX3UroyYf52L+2iVTrda8XW
# esPG62Mnn3T8AuLfzeJFuAbfOSERx7IFZO92UPoXE1uEjL5skl1yTZB3MubgOA4F
# 8KoRNhviFAEST+nG8c8uIsbZeb08SeYQMqjVEmkwggd6MIIFYqADAgECAgphDpDS
# AAAAAAADMA0GCSqGSIb3DQEBCwUAMIGIMQswCQYDVQQGEwJVUzETMBEGA1UECBMK
# V2FzaGluZ3RvbjEQMA4GA1UEBxMHUmVkbW9uZDEeMBwGA1UEChMVTWljcm9zb2Z0
# IENvcnBvcmF0aW9uMTIwMAYDVQQDEylNaWNyb3NvZnQgUm9vdCBDZXJ0aWZpY2F0
# ZSBBdXRob3JpdHkgMjAxMTAeFw0xMTA3MDgyMDU5MDlaFw0yNjA3MDgyMTA5MDla
# MH4xCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQHEwdS
# ZWRtb25kMR4wHAYDVQQKExVNaWNyb3NvZnQgQ29ycG9yYXRpb24xKDAmBgNVBAMT
# H01pY3Jvc29mdCBDb2RlIFNpZ25pbmcgUENBIDIwMTEwggIiMA0GCSqGSIb3DQEB
# AQUAA4ICDwAwggIKAoICAQCr8PpyEBwurdhuqoIQTTS68rZYIZ9CGypr6VpQqrgG
# OBoESbp/wwwe3TdrxhLYC/A4wpkGsMg51QEUMULTiQ15ZId+lGAkbK+eSZzpaF7S
# 35tTsgosw6/ZqSuuegmv15ZZymAaBelmdugyUiYSL+erCFDPs0S3XdjELgN1q2jz
# y23zOlyhFvRGuuA4ZKxuZDV4pqBjDy3TQJP4494HDdVceaVJKecNvqATd76UPe/7
# 4ytaEB9NViiienLgEjq3SV7Y7e1DkYPZe7J7hhvZPrGMXeiJT4Qa8qEvWeSQOy2u
# M1jFtz7+MtOzAz2xsq+SOH7SnYAs9U5WkSE1JcM5bmR/U7qcD60ZI4TL9LoDho33
# X/DQUr+MlIe8wCF0JV8YKLbMJyg4JZg5SjbPfLGSrhwjp6lm7GEfauEoSZ1fiOIl
# XdMhSz5SxLVXPyQD8NF6Wy/VI+NwXQ9RRnez+ADhvKwCgl/bwBWzvRvUVUvnOaEP
# 6SNJvBi4RHxF5MHDcnrgcuck379GmcXvwhxX24ON7E1JMKerjt/sW5+v/N2wZuLB
# l4F77dbtS+dJKacTKKanfWeA5opieF+yL4TXV5xcv3coKPHtbcMojyyPQDdPweGF
# RInECUzF1KVDL3SV9274eCBYLBNdYJWaPk8zhNqwiBfenk70lrC8RqBsmNLg1oiM
# CwIDAQABo4IB7TCCAekwEAYJKwYBBAGCNxUBBAMCAQAwHQYDVR0OBBYEFEhuZOVQ
# BdOCqhc3NyK1bajKdQKVMBkGCSsGAQQBgjcUAgQMHgoAUwB1AGIAQwBBMAsGA1Ud
# DwQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB8GA1UdIwQYMBaAFHItOgIxkEO5FAVO
# 4eqnxzHRI4k0MFoGA1UdHwRTMFEwT6BNoEuGSWh0dHA6Ly9jcmwubWljcm9zb2Z0
# LmNvbS9wa2kvY3JsL3Byb2R1Y3RzL01pY1Jvb0NlckF1dDIwMTFfMjAxMV8wM18y
# Mi5jcmwwXgYIKwYBBQUHAQEEUjBQME4GCCsGAQUFBzAChkJodHRwOi8vd3d3Lm1p
# Y3Jvc29mdC5jb20vcGtpL2NlcnRzL01pY1Jvb0NlckF1dDIwMTFfMjAxMV8wM18y
# Mi5jcnQwgZ8GA1UdIASBlzCBlDCBkQYJKwYBBAGCNy4DMIGDMD8GCCsGAQUFBwIB
# FjNodHRwOi8vd3d3Lm1pY3Jvc29mdC5jb20vcGtpb3BzL2RvY3MvcHJpbWFyeWNw
# cy5odG0wQAYIKwYBBQUHAgIwNB4yIB0ATABlAGcAYQBsAF8AcABvAGwAaQBjAHkA
# XwBzAHQAYQB0AGUAbQBlAG4AdAAuIB0wDQYJKoZIhvcNAQELBQADggIBAGfyhqWY
# 4FR5Gi7T2HRnIpsLlhHhY5KZQpZ90nkMkMFlXy4sPvjDctFtg/6+P+gKyju/R6mj
# 82nbY78iNaWXXWWEkH2LRlBV2AySfNIaSxzzPEKLUtCw/WvjPgcuKZvmPRul1LUd
# d5Q54ulkyUQ9eHoj8xN9ppB0g430yyYCRirCihC7pKkFDJvtaPpoLpWgKj8qa1hJ
# Yx8JaW5amJbkg/TAj/NGK978O9C9Ne9uJa7lryft0N3zDq+ZKJeYTQ49C/IIidYf
# wzIY4vDFLc5bnrRJOQrGCsLGra7lstnbFYhRRVg4MnEnGn+x9Cf43iw6IGmYslmJ
# aG5vp7d0w0AFBqYBKig+gj8TTWYLwLNN9eGPfxxvFX1Fp3blQCplo8NdUmKGwx1j
# NpeG39rz+PIWoZon4c2ll9DuXWNB41sHnIc+BncG0QaxdR8UvmFhtfDcxhsEvt9B
# xw4o7t5lL+yX9qFcltgA1qFGvVnzl6UJS0gQmYAf0AApxbGbpT9Fdx41xtKiop96
# eiL6SJUfq/tHI4D1nvi/a7dLl+LrdXga7Oo3mXkYS//WsyNodeav+vyL6wuA6mk7
# r/ww7QRMjt/fdW1jkT3RnVZOT7+AVyKheBEyIXrvQQqxP/uozKRdwaGIm1dxVk5I
# RcBCyZt2WwqASGv9eZ/BvW1taslScxMNelDNMYIZgjCCGX4CAQEwgZUwfjELMAkG
# A1UEBhMCVVMxEzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNVBAcTB1JlZG1vbmQx
# HjAcBgNVBAoTFU1pY3Jvc29mdCBDb3Jwb3JhdGlvbjEoMCYGA1UEAxMfTWljcm9z
# b2Z0IENvZGUgU2lnbmluZyBQQ0EgMjAxMQITMwAAAlKLM6r4lfM52wAAAAACUjAN
# BglghkgBZQMEAgEFAKCBrjAZBgkqhkiG9w0BCQMxDAYKKwYBBAGCNwIBBDAcBgor
# BgEEAYI3AgELMQ4wDAYKKwYBBAGCNwIBFTAvBgkqhkiG9w0BCQQxIgQgzO7XOsoT
# yVKdy3A9vuF7HjbvXJAxBmVx7D9ZeUZ7NU8wQgYKKwYBBAGCNwIBDDE0MDKgFIAS
# AE0AaQBjAHIAbwBzAG8AZgB0oRqAGGh0dHA6Ly93d3cubWljcm9zb2Z0LmNvbTAN
# BgkqhkiG9w0BAQEFAASCAQCE4JFRuovh5IXwZ5Fx2oGVi7jehmINqcypOPo5NQue
# XjKfGC5hJn0eepx5LceR85k/KeBg5FCh6SRz/EZlrvpFpFRS8HkR6wyr2A0KjMK2
# SgGQb5PB/EkwebTqWdEgUtqKCPyTwnGCzcpYZ7wQA/F4kiSUXlvjiNkPYPx58o91
# 5ihlBe/ljf0Oc7ujrjzrKRsp60pdXryGG8lns9EV/ay5ZpZrHYdDdrxWzlxdRuyN
# KABB5xOUGecDaR3cuR3bWJgQfUg9kY7RzQIqJPq3wtprzyC3LchfrLg4byAfxnLk
# A/mDj+TqQ0cGD3vJ+7rBl0lsbaqq13T4EB7aDwFzIHCKoYIXDDCCFwgGCisGAQQB
# gjcDAwExghb4MIIW9AYJKoZIhvcNAQcCoIIW5TCCFuECAQMxDzANBglghkgBZQME
# AgEFADCCAVUGCyqGSIb3DQEJEAEEoIIBRASCAUAwggE8AgEBBgorBgEEAYRZCgMB
# MDEwDQYJYIZIAWUDBAIBBQAEIJZLE81oQrqtWxZ3a50Lo0lmFXXNKEaHCctDxYnh
# KRLtAgZia0UTArwYEzIwMjIwNTA1MjEwODQ2LjYwOFowBIACAfSggdSkgdEwgc4x
# CzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQHEwdSZWRt
# b25kMR4wHAYDVQQKExVNaWNyb3NvZnQgQ29ycG9yYXRpb24xKTAnBgNVBAsTIE1p
# Y3Jvc29mdCBPcGVyYXRpb25zIFB1ZXJ0byBSaWNvMSYwJAYDVQQLEx1UaGFsZXMg
# VFNTIEVTTjowQTU2LUUzMjktNEQ0RDElMCMGA1UEAxMcTWljcm9zb2Z0IFRpbWUt
# U3RhbXAgU2VydmljZaCCEV8wggcQMIIE+KADAgECAhMzAAABpzW7LsJkhVApAAEA
# AAGnMA0GCSqGSIb3DQEBCwUAMHwxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpXYXNo
# aW5ndG9uMRAwDgYDVQQHEwdSZWRtb25kMR4wHAYDVQQKExVNaWNyb3NvZnQgQ29y
# cG9yYXRpb24xJjAkBgNVBAMTHU1pY3Jvc29mdCBUaW1lLVN0YW1wIFBDQSAyMDEw
# MB4XDTIyMDMwMjE4NTEyMloXDTIzMDUxMTE4NTEyMlowgc4xCzAJBgNVBAYTAlVT
# MRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQHEwdSZWRtb25kMR4wHAYDVQQK
# ExVNaWNyb3NvZnQgQ29ycG9yYXRpb24xKTAnBgNVBAsTIE1pY3Jvc29mdCBPcGVy
# YXRpb25zIFB1ZXJ0byBSaWNvMSYwJAYDVQQLEx1UaGFsZXMgVFNTIEVTTjowQTU2
# LUUzMjktNEQ0RDElMCMGA1UEAxMcTWljcm9zb2Z0IFRpbWUtU3RhbXAgU2Vydmlj
# ZTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAO0jOMYdUAXecCWm5V6T
# RoQZ4hsPLe0Vp6CwxFiTA5l867fAbDyxnKzdfBsf/0XJVXzIkcvzCESXoklvMDBD
# a97SEv+CuLEIooMbFBH1WeYgmLVO9TbbLStJilNITmQQQ4FB5qzMEsDfpmaZZMWW
# gdOjoSQed9UrjjmcuWsSskntiaUD/VQdQcLMnpeUGc7CQsAYo9HcIMb1H8DTcZ7y
# Ae3aOYf766P2OT553/4hdnJ9Kbp/FfDeUAVYuEc1wZlmbPdRa/uCx4iKXpt80/5w
# oAGSDl8vSNFxi4umXKCkwWHm8GeDZ3tOKzMIcIY/64FtpdqpNwbqGa3GkJToEFPR
# 6D6XJ0WyqebZvOZjMQEeLCJIrSnF4LbkkfkX4D4scjKz92lI9LRurhMPTBEQ6pw3
# iGsEPY+Jrcx/DJmyQWqbpN3FskWu9xhgzYoYsRuisCb5FIMShiallzEzum5xLE4U
# 5fuxEbwk0uY9ZVDNVfEhgiQedcSAd3GWvVM36gtYy6QJfixD7ltwjSm5sVa1voBf
# 2WZgCC3r4RE7VnovlqbCd3nHyXv5+8UGTLq7qRdRQQaBQXekT9UjUubcNS8ZYeZw
# K8d2etD98mSI4MqXcMySRKUJ9OZVQNWzI3LyS5+CjIssBHdv19aM6CjXQuZkkmlZ
# OtMqkLRg1tmhgI61yFC+jxB3AgMBAAGjggE2MIIBMjAdBgNVHQ4EFgQUH2y4fwWY
# LjCFb+EOQgPz9PpaRYMwHwYDVR0jBBgwFoAUn6cVXQBeYl2D9OXSZacbUzUZ6XIw
# XwYDVR0fBFgwVjBUoFKgUIZOaHR0cDovL3d3dy5taWNyb3NvZnQuY29tL3BraW9w
# cy9jcmwvTWljcm9zb2Z0JTIwVGltZS1TdGFtcCUyMFBDQSUyMDIwMTAoMSkuY3Js
# MGwGCCsGAQUFBwEBBGAwXjBcBggrBgEFBQcwAoZQaHR0cDovL3d3dy5taWNyb3Nv
# ZnQuY29tL3BraW9wcy9jZXJ0cy9NaWNyb3NvZnQlMjBUaW1lLVN0YW1wJTIwUENB
# JTIwMjAxMCgxKS5jcnQwDAYDVR0TAQH/BAIwADATBgNVHSUEDDAKBggrBgEFBQcD
# CDANBgkqhkiG9w0BAQsFAAOCAgEATxL6MfPZOhR91DHShlzal7B8vOCUvzlvbVha
# 0UzhZfvIcZA/bT3XTXbQPLnIDWlRdjQX7PGkORhX/mpjZCC5J7fD3TJMn9ZQQ8MX
# nJ0sx3/QJIlNgPVaOpk9Yk1YEqyItOyPHr3Om3v/q9h5f5qDk0IMV2taosze0JGl
# M3M5z7bGkDly+TfhH9lI03D/FzLjjzW8EtvcqmmH68QHdTsl84NWGkd2dUlVF2aB
# WMUprb8H9EhPUQcBcpf11IAj+f04yB3ncQLh+P+PSS2kxNLLeRg9CWbmsugplYP1
# D5wW+aH2mdyBlPXZMIaERJFvZUZyD8RfJ8AsE3uU3JSd408QBDaXDUf94Ki3wEXT
# tl8JQItGc3ixRYWNIghraI4h3d/+266OB6d0UM2iBXSqwz8tdj+xSST6G7ZYqxat
# Ezt806T1BBHe9tZ/mr2S52UjJgAVQBgCQiiiixNO27g5Qy4CDS94vT4nfC2lXwLl
# hrAcNqnAJKmRqK8ehI50TTIZGONhdhGcM5xUVeHmeRy9G6ufU6B6Ob0rW6LXY2qT
# LXvgt9/x/XEh1CrnuWeBWa9E307AbePaBopu8+WnXjXy6N01j/AVBq1TyKnQX1nS
# MjU9gZ3EaG8oS/zNM59HK/IhnAzWeVcdBYrq/hsu9JMvBpF+ZEQY2ZWpbEJm7ELl
# /CuRIPAwggdxMIIFWaADAgECAhMzAAAAFcXna54Cm0mZAAAAAAAVMA0GCSqGSIb3
# DQEBCwUAMIGIMQswCQYDVQQGEwJVUzETMBEGA1UECBMKV2FzaGluZ3RvbjEQMA4G
# A1UEBxMHUmVkbW9uZDEeMBwGA1UEChMVTWljcm9zb2Z0IENvcnBvcmF0aW9uMTIw
# MAYDVQQDEylNaWNyb3NvZnQgUm9vdCBDZXJ0aWZpY2F0ZSBBdXRob3JpdHkgMjAx
# MDAeFw0yMTA5MzAxODIyMjVaFw0zMDA5MzAxODMyMjVaMHwxCzAJBgNVBAYTAlVT
# MRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQHEwdSZWRtb25kMR4wHAYDVQQK
# ExVNaWNyb3NvZnQgQ29ycG9yYXRpb24xJjAkBgNVBAMTHU1pY3Jvc29mdCBUaW1l
# LVN0YW1wIFBDQSAyMDEwMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA
# 5OGmTOe0ciELeaLL1yR5vQ7VgtP97pwHB9KpbE51yMo1V/YBf2xK4OK9uT4XYDP/
# XE/HZveVU3Fa4n5KWv64NmeFRiMMtY0Tz3cywBAY6GB9alKDRLemjkZrBxTzxXb1
# hlDcwUTIcVxRMTegCjhuje3XD9gmU3w5YQJ6xKr9cmmvHaus9ja+NSZk2pg7uhp7
# M62AW36MEBydUv626GIl3GoPz130/o5Tz9bshVZN7928jaTjkY+yOSxRnOlwaQ3K
# Ni1wjjHINSi947SHJMPgyY9+tVSP3PoFVZhtaDuaRr3tpK56KTesy+uDRedGbsoy
# 1cCGMFxPLOJiss254o2I5JasAUq7vnGpF1tnYN74kpEeHT39IM9zfUGaRnXNxF80
# 3RKJ1v2lIH1+/NmeRd+2ci/bfV+AutuqfjbsNkz2K26oElHovwUDo9Fzpk03dJQc
# NIIP8BDyt0cY7afomXw/TNuvXsLz1dhzPUNOwTM5TI4CvEJoLhDqhFFG4tG9ahha
# YQFzymeiXtcodgLiMxhy16cg8ML6EgrXY28MyTZki1ugpoMhXV8wdJGUlNi5UPkL
# iWHzNgY1GIRH29wb0f2y1BzFa/ZcUlFdEtsluq9QBXpsxREdcu+N+VLEhReTwDwV
# 2xo3xwgVGD94q0W29R6HXtqPnhZyacaue7e3PmriLq0CAwEAAaOCAd0wggHZMBIG
# CSsGAQQBgjcVAQQFAgMBAAEwIwYJKwYBBAGCNxUCBBYEFCqnUv5kxJq+gpE8RjUp
# zxD/LwTuMB0GA1UdDgQWBBSfpxVdAF5iXYP05dJlpxtTNRnpcjBcBgNVHSAEVTBT
# MFEGDCsGAQQBgjdMg30BATBBMD8GCCsGAQUFBwIBFjNodHRwOi8vd3d3Lm1pY3Jv
# c29mdC5jb20vcGtpb3BzL0RvY3MvUmVwb3NpdG9yeS5odG0wEwYDVR0lBAwwCgYI
# KwYBBQUHAwgwGQYJKwYBBAGCNxQCBAweCgBTAHUAYgBDAEEwCwYDVR0PBAQDAgGG
# MA8GA1UdEwEB/wQFMAMBAf8wHwYDVR0jBBgwFoAU1fZWy4/oolxiaNE9lJBb186a
# GMQwVgYDVR0fBE8wTTBLoEmgR4ZFaHR0cDovL2NybC5taWNyb3NvZnQuY29tL3Br
# aS9jcmwvcHJvZHVjdHMvTWljUm9vQ2VyQXV0XzIwMTAtMDYtMjMuY3JsMFoGCCsG
# AQUFBwEBBE4wTDBKBggrBgEFBQcwAoY+aHR0cDovL3d3dy5taWNyb3NvZnQuY29t
# L3BraS9jZXJ0cy9NaWNSb29DZXJBdXRfMjAxMC0wNi0yMy5jcnQwDQYJKoZIhvcN
# AQELBQADggIBAJ1VffwqreEsH2cBMSRb4Z5yS/ypb+pcFLY+TkdkeLEGk5c9MTO1
# OdfCcTY/2mRsfNB1OW27DzHkwo/7bNGhlBgi7ulmZzpTTd2YurYeeNg2LpypglYA
# A7AFvonoaeC6Ce5732pvvinLbtg/SHUB2RjebYIM9W0jVOR4U3UkV7ndn/OOPcbz
# aN9l9qRWqveVtihVJ9AkvUCgvxm2EhIRXT0n4ECWOKz3+SmJw7wXsFSFQrP8DJ6L
# GYnn8AtqgcKBGUIZUnWKNsIdw2FzLixre24/LAl4FOmRsqlb30mjdAy87JGA0j3m
# Sj5mO0+7hvoyGtmW9I/2kQH2zsZ0/fZMcm8Qq3UwxTSwethQ/gpY3UA8x1RtnWN0
# SCyxTkctwRQEcb9k+SS+c23Kjgm9swFXSVRk2XPXfx5bRAGOWhmRaw2fpCjcZxko
# JLo4S5pu+yFUa2pFEUep8beuyOiJXk+d0tBMdrVXVAmxaQFEfnyhYWxz/gq77EFm
# PWn9y8FBSX5+k77L+DvktxW/tM4+pTFRhLy/AsGConsXHRWJjXD+57XQKBqJC482
# 2rpM+Zv/Cuk0+CQ1ZyvgDbjmjJnW4SLq8CdCPSWU5nR0W2rRnj7tfqAxM328y+l7
# vzhwRNGQ8cirOoo6CGJ/2XBjU02N7oJtpQUQwXEGahC0HVUzWLOhcGbyoYIC0jCC
# AjsCAQEwgfyhgdSkgdEwgc4xCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpXYXNoaW5n
# dG9uMRAwDgYDVQQHEwdSZWRtb25kMR4wHAYDVQQKExVNaWNyb3NvZnQgQ29ycG9y
# YXRpb24xKTAnBgNVBAsTIE1pY3Jvc29mdCBPcGVyYXRpb25zIFB1ZXJ0byBSaWNv
# MSYwJAYDVQQLEx1UaGFsZXMgVFNTIEVTTjowQTU2LUUzMjktNEQ0RDElMCMGA1UE
# AxMcTWljcm9zb2Z0IFRpbWUtU3RhbXAgU2VydmljZaIjCgEBMAcGBSsOAwIaAxUA
# wH7vHimSAzeDLN0qzWNb2p2vRH+ggYMwgYCkfjB8MQswCQYDVQQGEwJVUzETMBEG
# A1UECBMKV2FzaGluZ3RvbjEQMA4GA1UEBxMHUmVkbW9uZDEeMBwGA1UEChMVTWlj
# cm9zb2Z0IENvcnBvcmF0aW9uMSYwJAYDVQQDEx1NaWNyb3NvZnQgVGltZS1TdGFt
# cCBQQ0EgMjAxMDANBgkqhkiG9w0BAQUFAAIFAOYeVS4wIhgPMjAyMjA1MDUxNzUy
# NDZaGA8yMDIyMDUwNjE3NTI0NlowdzA9BgorBgEEAYRZCgQBMS8wLTAKAgUA5h5V
# LgIBADAKAgEAAgIMXQIB/zAHAgEAAgIR+zAKAgUA5h+mrgIBADA2BgorBgEEAYRZ
# CgQCMSgwJjAMBgorBgEEAYRZCgMCoAowCAIBAAIDB6EgoQowCAIBAAIDAYagMA0G
# CSqGSIb3DQEBBQUAA4GBAAA53uRjjcr2wAzTPwoKqK6pgR5wSAtBRLwHlg69hWeM
# FbUO6D32bH17oT7SznW9IVvGCDPw/+jGE80+N+GeV+q3IIzliD09st4+Uh1y+tTY
# dsD+h1sUk9LX8oAYaZ1V7QBJwFB/+bT1GQeFI0pL2E6CpLMUFkw7J72WLDfkoL4c
# MYIEDTCCBAkCAQEwgZMwfDELMAkGA1UEBhMCVVMxEzARBgNVBAgTCldhc2hpbmd0
# b24xEDAOBgNVBAcTB1JlZG1vbmQxHjAcBgNVBAoTFU1pY3Jvc29mdCBDb3Jwb3Jh
# dGlvbjEmMCQGA1UEAxMdTWljcm9zb2Z0IFRpbWUtU3RhbXAgUENBIDIwMTACEzMA
# AAGnNbsuwmSFUCkAAQAAAacwDQYJYIZIAWUDBAIBBQCgggFKMBoGCSqGSIb3DQEJ
# AzENBgsqhkiG9w0BCRABBDAvBgkqhkiG9w0BCQQxIgQg6gkghZWTsDWCA4b3sTL+
# +53m18+rSHvASo7NZ6My8qEwgfoGCyqGSIb3DQEJEAIvMYHqMIHnMIHkMIG9BCBH
# 8H/nCZUC4L0Yqbz3sH3w5kzhwJ4RqCkXXKxNPtqOGzCBmDCBgKR+MHwxCzAJBgNV
# BAYTAlVTMRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQHEwdSZWRtb25kMR4w
# HAYDVQQKExVNaWNyb3NvZnQgQ29ycG9yYXRpb24xJjAkBgNVBAMTHU1pY3Jvc29m
# dCBUaW1lLVN0YW1wIFBDQSAyMDEwAhMzAAABpzW7LsJkhVApAAEAAAGnMCIEIPMs
# ZPs2GSagl/0O6pus/fCQs3j238q9JTT70PoO6xZnMA0GCSqGSIb3DQEBCwUABIIC
# ABbllr1N4O70eY/PkLh7klY/0US53KXDiCPrn0xpkBkKjldbyaujBqAIavuh9jCl
# 9EV5fnfxVKi1UiqHIYjCq9LHpaoQCaRO+9/8QTvQnjYVjS8iPRxExWOdSpDD9Rqr
# d/xpLE2DfjY+NuvhNvGyvPqHZogNwTiExOiVK9XxHbk+9x6WGb1Tx2RNSAvfB2wQ
# VWcsNI+mhdxjNNQlQizjfHrWLaaLoC3j+f33uv2Sy26ofEM6CCs3gS7Cc6oUrGoJ
# MzzHtFu3q8/s7HNwUUClOT/k3mbLDncMuuJhYPEN+BM4AHyYEAg2AXOq82zuokD6
# Pn/15t0ELWUjfR46Us8ApGuvXWp+4n4Zk2j0lyMb7DhqYnqAeXTiRlqImchVXnBJ
# BM0j9aJGuz1Ee47mSKL79KdBXgThLJeW7ESc+JDICtOGK0WQOKihUCZ7ZZzm9Vby
# rglxEhBYASv1wARogUp3ASBB1URz3FvtVLkKSkWBuCl4fJu417xaz1AoyxB2+KpM
# IKkSFPSP9dsfYJqJFUgiaLpesVWS/KUPYGIJoWF+8ap9ajMxBI7FmI/uW25dKvnX
# fhuUZFTI8fyDyUW1g6/RdSy/gzLpyZQkXBbMxgEoG2VqkRvkZKauWpcJDgfmV29q
# nvgISNYgR6YaqV8BW5NWLtYvF7i+88GlxBX8sgAb/GSo
# SIG # End signature block
