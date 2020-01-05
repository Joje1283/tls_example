# tls_example
tls_example in python

## openssl command
### source - https://namjackson.tistory.com/24
<pre><code># 개인키, 공개키 발급 과정 - private.key, public.key
$ openssl genrsa -des3 -out private.key 2048 // 개인키
$ openssl genrsa -out private.key 2048 // 비밀번호 없는 개인키 (선택사항)
$ openssl rsa -in private.key -pubout -out public.key

# CSR(인증요청서: SSL인증의 정보를 암호화하여 인증기관에 보내 인증서를 발급받게 하는 신청서. 국가코드, 도시, 회사명, 부서명, 이메일, 도메인주소 등이 있음.) 만들기 - private.csr
$ openssl req -new -key private.key -out private.csr

# CRT(인증서)만들기. - private.crt)
## 사설 CA로부터 인증받은 인증서를 만들기 위해서 서명을 해줄 rootCA를 생성한다.
$ openssl genrsa -aes256 -out rootCA.key 2048

## rootCA 사설 CSR 생성하기 - rootCA.key를 이용해서 10년짜리 rootCA.pem(이게 CSR인듯>)을 생성.
$ openssl req -x509 -new -nodes -key rootCA.key -days 3650 -out rootCA.pem

## CRT 생성 - CSR(private.csr)을 커스텀CA인 rootCA의 인증을 받아(rootCA.key, rootCA.pem) 인증서(private.crt)를 생성한다.
$ openssl x509 -req -in private.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out private.crt -days 3650
</code></pre>
