# tls_example
tls_example in python



## openssl command
source: https://mylko72.gitbooks.io/node-js/content/chapter8/chapter8_4.html

TLS 서버와 클라이언트를 구현하기 위해서는 양쪽에서 개인키와 공개인증서를 생성해야 한다.  
openSSL을 이용해서 다음과 같이 생성할 수 있다.

<pre><code>$ openssl genrsa -out server.pem 2048  // 개인키 생성 (server.pem
$ openssl req -new -key server.pem -out server.csr  // 서명한 인증파일 생성 (server.csr)
$ openssl x509 -req -days 365 -in server.csr -signkey server.pem -out server.crt // 자신이 서명한 인증서 생성 (server.crt)
</code></pre>

클리아언트도 위와 같은 같은 방법으로 생성한다.
