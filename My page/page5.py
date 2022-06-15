# Hello World project 
# python3
# tarekh tavalod and rooz 
# محاسبه تاریخ تولد به روز
Month = [ 'Farvardin','Ordibehesht', 'Khordad','Tir', 'Mordad', 'Shahrivar', 'Mehr', 'Aban', 'Azar', 'Day', 'Bahman', 'Esfand']

Y = int(input('\nEnter year:'))
M = int(input('\nEnter Month:'))
D = int(input('\nEnter Day:'))

end = ['st' ,  'nd' ,  'rd'] + 17*['th'] + [ 'st' , 'nd' , 'rd'] +7 * ['th'] + ['st']

m_index = M-1
d_index = D-1

print (D, end[d_index] ,   ' ' ,  Month [m_index] ,   ' ' ,  Y)
