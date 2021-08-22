down_the_line = '\n'+'\n'+'\n'
empty = ' '*42
import os
def enternumber(s = str()):#nhập số(nếu quán trình nhập số mà vô tình chứa kí tự số thì nó sẻ yêu cầu nhập lại)
    while True:
        print(empty  ,end= ' ')
        n = input(' Nhập %s'%s)
        if n.isdigit():
            break
    return n

def enterword(s = str()):#nhập chữ( trong quá trình bạn nhập chứ nếu xuất hiện kí tự số thị nó sẻ yêu cầu nhập lại)
    print(empty,end='')
    n = input('  Nhập %s'%s)
    while any(i.isdigit() for i in n):
        print(empty,end='')
        n = input('  Nhập lại %s'%s)
    return n

def enternumberfloat(s = str()):#nhập số float
    print(empty,end='')
    n = input('  Nhập %s'%s)
    while any(i.isalpha() for i in n):
        print(empty,end='')
        n = input('  Nhập lại %s'%s)
    return n

def  caculator():#Tính toán cộng trừ nhân chia
    print(empty,' Nhập * để thực hiện phép tính nhân ')
    print(empty,' Nhập - để thực hiện phép tính trừ')
    print(empty,' Nhập + để thực hiện phép tính nhân ')
    print(empty,' Nhập \ để thực hiện phép tính chia ')
    def tinh(a,dauu,b):
        if  dauu=='+':
            return a+b
        elif    dauu=='-':
            return a-b
        elif    dauu=='/':
            if b==0:
                return 'Lỗi'
            return a/b
        elif dauu=='*':
            return a*b
        else:
            return 'Lỗi'
    def nhap():
        print(empty ,end= ' ')
        a=int(enternumber('số: '))
        print(empty ,end= ' ')
        dauu = input(' Nhập dấu: ')
        print(empty ,end= ' ')
        b=int(input(' Nhập số: '))
        print(empty,' kết quả là: ',tinh(a,dauu,b))
    nhap()

def score_caculator():#tính điểm trung bình môn(đã hoàn chỉnh)
    def in_ra(core,mon,total_score,hs,n):
        print('\n'+empty,end=' ')
        print(' ĐÂY LÀ KẾT QUẢ CỦA CHÚNG TÔI ')
        print('\n'+empty,end=' ')
        for j in range(len(core)):

            print(' Môn '+str((mon[j])) +' là: '+ str((core[j])),end='   ')
        print()
        print(empty +'  Điểm trung bình ' +str(n) +' môn của bạn là: ',total_score / hs)
        print(empty +'  Tổng hệ số  ' +str(n) +' môn của bạn là: ',hs)
    def nhap_tinh():

        hs = 0
        total_score = 0
        mon = []
        core = []
        n=int(enternumber('số môn: '))
        while n  <0:
            n=int(enternumber('lại số môn lớn hơn 0:  '))
        for i in range(1,n+1):            
            namemon = enterword('tên môn là %d : '%i ).title()
            while True:
                score = float(enternumberfloat('điểm môn %s  là:'%namemon ))
                if score >= 0 and score <= 10:
                    break
                else:
                    print(empty + '  Điểm bạn vừa Nhập bị lỗi')
            while True:
                heso = float(enternumberfloat('hệ số của môn %s là: '%namemon))
                if heso in (1,1.5,2,2.5,3):
                    break
            total_score += score * heso
            hs += heso 
            mon += [namemon]
            core += [score]
        in_ra(core,mon,total_score,hs,n)
    nhap_tinh()

def employee_information():#thông tin nhân viên (đã hoàn chỉnh)
    yeare = str(enterword( 'tên: ' ))
    yearecapital = yeare.title()# title: lam in hoa chu cai đầu tiên sau khoảng trắng, hàm 'capitalize là hàm in hoa chữ cái đầu tiên trong chỗi
    detached_yeare = yearecapital.rsplit(' ',1)# hàm split dùng để tách chuỗi từ trái sang phải và rsplit tah chuỗi từ phải sang trái (cú pháp là : chuỗi.split('khoản trắng',và vị trí dấu trắng để phân cách)
    print(empty + '  Họ tên lót: ',detached_yeare[0] )
    print(empty + '  Tên: ' ,detached_yeare[1] )
    print(empty + '  Họ tên đầy đủ: ',yearecapital)
    '''
    name = str(input('nhập tên: '))
    nameupper=name.title()
    nametach=nameupper.split()
    holot=''
    a=nametach[-1]
    for i in nametach[0:-1]:
        holot += i + ' '
    print('Họ tên lót là: ',holot)
    print('Tên là: ',a)
    print(' Họ tên đầy đủ là: ',nameupper)
    '''

def see_salary():# Xem lương nè (đã hoàn chỉnh)(# phần hiển thị chưa đẹp mắt)
    def lists(ten,total_luong):
        for i in range (len(total_luong)):
            for j in range (len(total_luong)):
                if total_luong[i] < total_luong[j]:
                    total_luong[i], total_luong[j] = total_luong[j], total_luong[i]
                    ten[i], ten[j] = ten[j], ten[i]        
        for t in range (len(total_luong)):
            print(empty+'  '+ str(t+1) +'|  ', ten[t],':', f'{int(total_luong[t]):,d}'+ ' vnđ')



    def nhap():
        ten = []
        total_luong = []
        
        n = int(enternumber('số lượng nhân viên: '))
    
        while n < 0:
            
            n = int(enternumber('số lượng nhân viên: '))
        for i in range(1,n+1):
            name = enterword('tên nhân viên %d : '%i).title()            
            salary = float(enternumberfloat('số lương nhân viên %s: '%name))
            ten += [name]
            total_luong += [salary] 
        print('\n'+'\n')      
        print(empty + '  DANH SÁCH TÊN VÀ LƯƠNG NHÂN VIÊN TỪ THẤP ĐẾN CAO ')    
        lists(ten,total_luong)
        
    nhap()

def payroll():# tính lương(đã hoàn chỉnh)

    def tinhluong(time,salary):
        s = 0
        if time <= 40:
            s = empty + '  Tổng sô lương là:' + f'{int(salary * time) : ,d} vnđ'
            return s
            
        else:
            s = empty + '  Tổng sô lương là:' +f'{int(40 * salary + (time-40)*1.5*salary):,d} vnđ'
            return s
            
    def nhap():
        
        time = float(enternumberfloat('số giờ làm việc:'))
        
        salary = float(enternumberfloat('số lương làm trong 1 giờ:'))
        print(tinhluong(time,salary))
    nhap()
    '''
        def tinhluongt(n):
        for i in range(1,n+1):
            name = input('Nhap tên nhan viên %d: '%i).title() #% i thay thế vào %d
            time = float(input('So gio lam cua %s: '%name)) #%name sẽ thay thế vào %s
            salary = int(input('So luong/gio cua %s: '%name))
            if h <= 40:
                print('Nhan vien', name,'co tong so luong la:', sh * h,'VND')
            else:
                print('Nhan vien', name,'co tong so luong la:',40 * sh + ( h - 40) * sh * 1.5),'VND'
    '''

def calander():#  Xem lịch   ( đã hoàn chỉnh)
    
    n = int(enternumber('tháng là : '))
    while n <1 or n >12:
        n = int(enternumber('lại số tháng từ 1 đến 12: '))
    year = int(enternumber('năm: '))
    while year <1 :
        year = int(enternumber('lại năm: '))
    print('\n'+'\n')
    print(empty+'  ĐÂY LÀ KẾT QUẢ MÀ CHÚNG TÔI ĐÃ XÁC THỰC')
    print()
    print(empty + '  Năm bạn vừa nhập là:  '+ str(year))
    print(empty + '  Tháng bạn vừa nhập là:  '+ str(n))  
    if n in (1,3,5,7,8,10,12):

        print(empty + '  Tháng này có 31 ngày')
    elif n in (4,6,9,11):

        print(empty +  '  Tháng này có 30 ngày ')
    else:
        
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:

            print(empty +'  Đây là năm nhuận'  '              Tháng này có 29 ngày')
        else:
            print(empty +  '  Tháng này có 28 ngày ')

def select():# hàm chọ chương trình
    while True:
        
        n = int(enternumber('số xin vui lòng chọn số :  '))
        os.system('cls')
        if n > 0 and n < 8:
            break
        print(empty  ,end= ' ')
        print('  Nhập lại nhé bạn ! ') 
    if n == 1:        
        print(down_the_line+ empty+26*'*'+' CHÀO MỪNG QUÝ KHÁCH ĐẾN VỚI CHƯƠNG TRÌNH XEM LỊCH '+26*'*'+down_the_line)
        calander()
    elif n == 2:        
        print(down_the_line+ empty+26*'*'+' CHÀO MỪNG QUÝ KHÁCH ĐẾN VỚI CHƯƠNG TRÌNH TÍNH  LƯƠNG '+26*'*'+down_the_line)
        payroll()
    elif n == 3:
        print(down_the_line+ empty+26*'*'+' CHÀO MỪNG QUÝ KHÁCH ĐẾN VỚI CHƯƠNG TRÌNH XEM LƯƠNG '+26*'*'+down_the_line)
        see_salary()
    elif n == 4:
        print(down_the_line+ empty+26*'*'+' CHÀO MỪNG QUÝ KHÁCH ĐẾN VỚI CHƯƠNG TRÌNH XEM THÔNG TIN NHÂN VIÊN '+26*'*'+down_the_line)
        employee_information()
    elif n == 5:
        print(down_the_line+ empty+24*'*'+' CHÀO MỪNG QUÝ KHÁCH ĐẾN VỚI CHƯƠNG TRÌNH TÍNH ĐIỂM TRUNG BÌNH '+24*'*'+down_the_line)
        score_caculator()
    elif n == 6:
        print(down_the_line+ empty+26*'*'+' CHÀO MỪNG QUÝ KHÁCH ĐẾN VỚI CHƯƠNG TRÌNH TÍNH TOÁN '+26*'*'+down_the_line)
        caculator()
    else:
        if n == 7:
            exit()

def menu(): # background
    
    b = '*'*100 + '\n'
    c = '*'*34+' CHƯƠNG TRÌNH THÔNG MINH '+'*'*41+'\n'
    d = '='*45+'MENU'+'='*51+ down_the_line
    e = 'Xin vui lòng chọn: '+'\n'+empty+2 *' '+'1. Xem lịch '+'\n'+empty+2 *' '+'2. Tính lương '+'\n'+empty+2 *' '+'3. xem lương  '+'\n' 
    f = '4. Xem thông tin nhân viên '+'\n'+empty+ 2*' '+'5. tính điểm học sinh '+'\n'+empty+2 *' '+'6. Tính toán cộng trừ nhân chia ' +'\n'+empty+2 *' '+'7. Thoát chương trình  '    
    print('',empty,b,empty,c,empty,b,empty,d,empty,e,empty,f)
    
    select()

while True:#begin
    menu()
    print(empty ,end= '  ')
    x = input( 'Bạn nhấn phím cách để thoát(nếu không thì chọn kí tự bất kì để tiếp tục với menu chính): ')
    
    if x == ' ':
        exit()
    os.system('cls')
   
