import qrcode

url1 = 'https://gulbiarchive.tistory.com/'
'''
make() 함수
QR 코드 생성
'''
qrcode_img = qrcode.make(url1)

'''
save() 함수
이미지 파일로 저장
'''
qrcode_img.save('./my_qrcode.png')