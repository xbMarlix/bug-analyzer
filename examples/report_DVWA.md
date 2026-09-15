# BugHunter Report: DVWA

**Generated:** 2026-09-15 15:45:13
**Project:** `/tmp/DVWA`
**Analyzers:** static

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 188 |
| Total lines | 14,433 |
| Bugs found | 58 |
| !!! Critical | 17 |
| !! High | 7 |
| ! Medium | 11 |
| ~ Low | 6 |
| i Info | 17 |

## Top Findings (10)

| Severity | File | Issue |
|----------|------|-------|
| CRITICAL | `login.php:39` | Hardcoded Secret |
| CRITICAL | `vulnerabilities/csrf/test_credentials.php:21` | Hardcoded Secret |
| CRITICAL | `vulnerabilities/sqli/test.php:4` | Hardcoded Secret |
| CRITICAL | `vulnerabilities/javascript/source/high.js:1` | Dangerous Code Execution |
| CRITICAL | `vulnerabilities/javascript/source/high_unobfuscated.js:83` | Dangerous Code Execution |
| CRITICAL | `vulnerabilities/csrf/source/low.php:16` | Hardcoded Secret |
| CRITICAL | `vulnerabilities/csrf/source/medium.php:18` | Hardcoded Secret |
| CRITICAL | `vulnerabilities/cryptography/source/token_library_high.php:37` | Hardcoded Secret |
| CRITICAL | `vulnerabilities/cryptography/source/token_library_impossible.php:40` | Hardcoded Secret |
| CRITICAL | `vulnerabilities/captcha/source/high.php:30` | Hardcoded Secret |

### Languages Detected

- **php**: 169 files
- **javascript**: 9 files
- **sql**: 5 files
- **css**: 5 files

## Security (21)

### [!!!] Hardcoded Secret

- **File:** `login.php:39`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      37 | 	}
      38 | 
>>>   39 | 	$query  = "SELECT * FROM `users` WHERE user='$user' AND password='$pass';";
      40 | 	$result = @mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '.<br />Try <a href="setup.php">installing again</a>.</pre>' );
      41 | 	if( $result && mysqli_num_rows( $result ) == 1 ) {    // Login Successful...
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/csrf/test_credentials.php:21`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      19 | 	$pass = md5( $pass );
      20 | 
>>>   21 | 	$query  = "SELECT * FROM `users` WHERE user='$user' AND password='$pass';";
      22 | 	$result = @mysqli_query($GLOBALS["___mysqli_ston"], $query) or die( '<pre>'.  mysqli_connect_error() . '.<br />Try <a href="setup.php">installing again</a>.</pre>' );
      23 | 	if( $result && mysqli_num_rows( $result ) == 1 ) {    // Login Successful...
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/sqli/test.php:4`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
       2 | $host = "192.168.0.7";
       3 | $username = "dvwa";
>>>    4 | $password = "password";
       5 | 
       6 | mssql_connect($host, $username, $password);
```
</details>

---

### [!!!] Dangerous Code Execution

- **File:** `vulnerabilities/javascript/source/high.js:1`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Dynamic code execution detected. This can lead to remote code execution vulnerabilities.

**Fix:** Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.

<details>
<summary>Code</summary>

```
>>>    1 | var a=['fromCharCode','toString','replace','BeJ','\x5cw+','Lyg','SuR','(w(){\x273M\x203L\x27;q\x201l=\x273K\x203I\x203J\x20T\x27;q\x201R=1c\x202I===\x271n\x27;q\x20Y=1R?2I:{};p(Y.3N){1R=1O}q\x202L=!1R&&1c\x202M===\x271n\x27;q\x202o=!Y.2S&&1c\x202d===\x271n\x27&&2d.2Q&&2d.2Q.3S;p(2o){Y=3R}z\x20p(2L){Y=2M}q\x202G=!Y.3Q&&1c\x202g===\x271n\x27&&2g.X;q\x202s=1c\x202l===\x27w\x27&&2l.3P;q\x201y=!Y.3H&&1c\x20Z!==\x272T\x27;q\x20m=\x273G\x27.3z(\x27\x27);q\x202w=[-3y,3x,3v,3w];q\x20U=[24,16,8,0];q\x20K=[3A,3B,3F,3E,3D,3C,3T,3U,4d,4c,4b,49,4a,4e,4f,4j,4i,4h,3u,48,47,3Z,3Y,3X,3V,3W,40,41,46,45,43,42,4k,3f,38,36,39,37,34,33,2Y,31,2Z,35,3t,3n,3m,3l,3o,3p,3s,3r,3q,3k,3j,3d,3a,3c,3b,3e,3h,3g,3i,4g];q\x201E=[\x271e\x27,\x2727\x27,\x271G\x27,\x272R\x27];q\x20l=[];p(Y.2S||!1z.1K){1z.1K=w(1x){A\x204C.Q.2U.1I(1x)===\x27[1n\x201z]\x27}}p(1y&&(Y.50||!Z.1N)){Z.1N=w(1x){A\x201c\x201x===\x271n\x27&&1x.1w&&1x.1w.1J===Z}}q\x202m=w(1X,x){A\x20w(s){A\x20O\x20N(x,1d).S(s)[1X]()}};q\x202a=w(x){q\x20P=2m(\x271e\x27,x);p(2o){P=2P(P,x)}P.1T=w(){A\x20O\x20N(x)};P.S=w(s){A\x20P.1T().S(s)};1g(q\x20i=0;i<1E.W;++i){q\x20T=1E[i];P[T]=2m(T,x)}A\x20P};q\x202P=w(P,x){q\x201S=2O(\x222N(\x271S\x27)\x22);q\x201Y=2O(\x222N(\x271w\x27).1Y\x22);q\x202n=x?\x271H\x27:\x271q\x27;q\x202z=w(s){p(1c\x20s===\x272p\x27){A\x201S.2x(2n).S(s,\x274S\x27).1G(\x271e\x27)}z{p(s===2q||s===2T){1u\x20O\x201t(1l)}z\x20p(s.1J===Z){s=O\x202r(s)}}p(1z.1K(s)||Z.1N(s)||s.1J===1Y){A\x201S.2x(2n).S(O\x201Y(s)).1G(\x271e\x27)}z{A\x20P(s)}};A\x202z};q\x202k=w(1X,x){A\x20w(G,s){A\x20O\x201P(G,x,1d).S(s)[1X]()}};q\x202f=w(x){q\x20P=2k(\x271e\x27,x);P.1T=w(G){A\x20O\x201P(G,x)};P.S=w(G,s){A\x20P.1T(G).S(s)};1g(q\x20i=0;i<1E.W;++i){q\x20T=1E[i];P[T]=2k(T,x)}A\x20P};w\x20N(x,1v){p(1v){l[0]=l[16]=l[1]=l[2]=l[3]=l[4]=l[5]=l[6]=l[7]=l[8]=l[9]=l[10]=l[11]=l[12]=l[13]=l[14]=l[15]=0;k.l=l}z{k.l=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}p(x){k.C=4I;k.B=4H;k.E=4l;k.F=4U;k.J=4J;k.I=4K;k.H=4L;k.D=4T}z{k.C=4X;k.B=4W;k.E=4Y;k.F=4Z;k.J=4V;k.I=4O;k.H=4F;k.D=4s}k.1C=k.1A=k.L=k.2i=0;k.1U=k.1L=1O;k.2j=1d;k.x=x}N.Q.S=w(s){p(k.1U){A}q\x202h,T=1c\x20s;p(T!==\x272p\x27){p(T===\x271n\x27){p(s===2q){1u\x20O\x201t(1l)}z\x20p(1y&&s.1J===Z){s=O\x202r(s)}z\x20p(!1z.1K(s)){p(!1y||!Z.1N(s)){1u\x20O\x201t(1l)}}}z{1u\x20O\x201t(1l)}2h=1d}q\x20r,M=0,i,W=s.W,l=k.l;4t(M<W){p(k.1L){k.1L=1O;l[0]=k.1C;l[16]=l[1]=l[2]=l[3]=l[4]=l[5]=l[6]=l[7]=l[8]=l[9]=l[10]=l[11]=l[12]=l[13]=l[14]=l[15]=0}p(2h){1g(i=k.1A;M<W&&i<1k;++M){l[i>>2]|=s[M]<<U[i++&3]}}z{1g(i=k.1A;M<W&&i<1k;++M){r=s.1Q(M);p(r<R){l[i>>2]|=r<<U[i++&3]}z\x20p(r<2v){l[i>>2]|=(2t|(r>>6))<<U[i++&3];l[i>>2]|=(R|(r&V))<<U[i++&3]}z\x20p(r<2A||r>=2E){l[i>>2]|=(2D|(r>>12))<<U[i++&3];l[i>>2]|=(R|((r>>6)&V))<<U[i++&3];l[i>>2]|=(R|(r&V))<<U[i++&3]}z{r=2C+(((r&23)<<10)|(s.1Q(++M)&23));l[i>>2]|=(2X|(r>>18))<<U[i++&3];l[i>>2]|=(R|((r>>12)&V))<<U[i++&3];l[i>>2]|=(R|((r>>6)&V))<<U[i++&3];l[i>>2]|=(R|(r&V))<<U[i++&3]}}}k.2u=i;k.L+=i-k.1A;p(i>=1k){k.1C=l[16];k.1A=i-1k;k.1W();k.1L=1d}z{k.1A=i}}p(k.L>4r){k.2i+=k.L/2H<<0;k.L=k.L%2H}A\x20k};N.Q.1s=w(){p(k.1U){A}k.1U=1d;q\x20l=k.l,i=k.2u;l[16]=k.1C;l[i>>2]|=2w[i&3];k.1C=l[16];p(i>=4q){p(!k.1L){k.1W()}l[0]=k.1C;l[16]=l[1]=l[2]=l[3]=l[4]=l[5]=l[6]=l[7]=l[8]=l[9]=l[10]=l[11]=l[12]=l[13]=l[14]=l[15]=0}l[14]=k.2i<<3|k.L>>>29;l[15]=k.L<<3;k.1W()};N.Q.1W=w(){q\x20a=k.C,b=k.B,c=k.E,d=k.F,e=k.J,f=k.I,g=k.H,h=k.D,l=k.l,j,1a,1b,1j,v,1f,1h,1B,1Z,1V,1D;1g(j=16;j<1k;++j){v=l[j-15];1a=((v>>>7)|(v<<25))^((v>>>18)|(v<<14))^(v>>>3);v=l[j-2];1b=((v>>>17)|(v<<15))^((v>>>19)|(v<<13))^(v>>>10);l[j]=l[j-16]+1a+l[j-7]+1b<<0}1D=b&c;1g(j=0;j<1k;j+=4){p(k.2j){p(k.x){1B=4m;v=l[0]-4n;h=v-4o<<0;d=v+4p<<0}z{1B=4v;v=l[0]-4w;h=v-4G<<0;d=v+4D<<0}k.2j=1O}z{1a=((a>>>2)|(a<<30))^((a>>>13)|(a<<19))^((a>>>22)|(a<<10));1b=((e>>>6)|(e<<26))^((e>>>11)|(e<<21))^((e>>>25)|(e<<7));1B=a&b;1j=1B^(a&c)^1D;1h=(e&f)^(~e&g);v=h+1b+1h+K[j]+l[j];1f=1a+1j;h=d+v<<0;d=v+1f<<0}1a=((d>>>2)|(d<<30))^((d>>>13)|(d<<19))^((d>>>22)|(d<<10));1b=((h>>>6)|(h<<26))^((h>>>11)|(h<<21))^((h>>>25)|(h<<7));1Z=d&a;1j=1Z^(d&b)^1B;1h=(h&e)^(~h&f);v=g+1b+1h+K[j+1]+l[j+1];1f=1a+1j;g=c+v<<0;c=v+1f<<0;1a=((c>>>2)|(c<<30))^((c>>>13)|(c<<19))^((c>>>22)|(c<<10));1b=((g>>>6)|(g<<26))^((g>>>11)|(g<<21))^((g>>>25)|(g<<7));1V=c&d;1j=1V^(c&a)^1Z;1h=(g&h)^(~g&e);v=f+1b+1h+K[j+2]+l[j+2];1f=1a+1j;f=b+v<<0;b=v+1f<<0;1a=((b>>>2)|(b<<30))^((b>>>13)|(b<<19))^((b>>>22)|(b<<10));1b=((f>>>6)|(f<<26))^((f>>>11)|(f<<21))^((f>>>25)|(f<<7));1D=b&c;1j=1D^(b&d)^1V;1h=(f&g)^(~f&h);v=e+1b+1h+K[j+3]+l[j+3];1f=1a+1j;e=a+v<<0;a=v+1f<<0}k.C=k.C+a<<0;k.B=k.B+b<<0;k.E=k.E+c<<0;k.F=k.F+d<<0;k.J=k.J+e<<0;k.I=k.I+f<<0;k.H=k.H+g<<0;k.D=k.D+h<<0};N.Q.1e=w(){k.1s();q\x20C=k.C,B=k.B,E=k.E,F=k.F,J=k.J,I=k.I,H=k.H,D=k.D;q\x201e=m[(C>>28)&o]+m[(C>>24)&o]+m[(C>>20)&o]+m[(C>>16)&o]+m[(C>>12)&o]+m[(C>>8)&o]+m[(C>>4)&o]+m[C&o]+m[(B>>28)&o]+m[(B>>24)&o]+m[(B>>20)&o]+m[(B>>16)&o]+m[(B>>12)&o]+m[(B>>8)&o]+m[(B>>4)&o]+m[B&o]+m[(E>>28)&o]+m[(E>>24)&o]+m[(E>>20)&o]+m[(E>>16)&o]+m[(E>>12)&o]+m[(E>>8)&o]+m[(E>>4)&o]+m[E&o]+m[(F>>28)&o]+m[(F>>24)&o]+m[(F>>20)&o]+m[(F>>16)&o]+m[(F>>12)&o]+m[(F>>8)&o]+m[(F>>4)&o]+m[F&o]+m[(J>>28)&o]+m[(J>>24)&o]+m[(J>>20)&o]+m[(J>>16)&o]+m[(J>>12)&o]+m[(J>>8)&o]+m[(J>>4)&o]+m[J&o]+m[(I>>28)&o]+m[(I>>24)&o]+m[(I>>20)&o]+m[(I>>16)&o]+m[(I>>12)&o]+m[(I>>8)&o]+m[(I>>4)&o]+m[I&o]+m[(H>>28)&o]+m[(H>>24)&o]+m[(H>>20)&o]+m[(H>>16)&o]+m[(H>>12)&o]+m[(H>>8)&o]+m[(H>>4)&o]+m[H&o];p(!k.x){1e+=m[(D>>28)&o]+m[(D>>24)&o]+m[(D>>20)&o]+m[(D>>16)&o]+m[(D>>12)&o]+m[(D>>8)&o]+m[(D>>4)&o]+m[D&o]}A\x201e};N.Q.2U=N.Q.1e;N.Q.1G=w(){k.1s();q\x20C=k.C,B=k.B,E=k.E,F=k.F,J=k.J,I=k.I,H=k.H,D=k.D;q\x202b=[(C>>24)&u,(C>>16)&u,(C>>8)&u,C&u,(B>>24)&u,(B>>16)&u,(B>>8)&u,B&u,(E>>24)&u,(E>>16)&u,(E>>8)&u,E&u,(F>>24)&u,(F>>16)&u,(F>>8)&u,F&u,(J>>24)&u,(J>>16)&u,(J>>8)&u,J&u,(I>>24)&u,(I>>16)&u,(I>>8)&u,I&u,(H>>24)&u,(H>>16)&u,(H>>8)&u,H&u];p(!k.x){2b.4A((D>>24)&u,(D>>16)&u,(D>>8)&u,D&u)}A\x202b};N.Q.27=N.Q.1G;N.Q.2R=w(){k.1s();q\x201w=O\x20Z(k.x?28:32);q\x201i=O\x204x(1w);1i.1p(0,k.C);1i.1p(4,k.B);1i.1p(8,k.E);1i.1p(12,k.F);1i.1p(16,k.J);1i.1p(20,k.I);1i.1p(24,k.H);p(!k.x){1i.1p(28,k.D)}A\x201w};w\x201P(G,x,1v){q\x20i,T=1c\x20G;p(T===\x272p\x27){q\x20L=[],W=G.W,M=0,r;1g(i=0;i<W;++i){r=G.1Q(i);p(r<R){L[M++]=r}z\x20p(r<2v){L[M++]=(2t|(r>>6));L[M++]=(R|(r&V))}z\x20p(r<2A||r>=2E){L[M++]=(2D|(r>>12));L[M++]=(R|((r>>6)&V));L[M++]=(R|(r&V))}z{r=2C+(((r&23)<<10)|(G.1Q(++i)&23));L[M++]=(2X|(r>>18));L[M++]=(R|((r>>12)&V));L[M++]=(R|((r>>6)&V));L[M++]=(R|(r&V))}}G=L}z{p(T===\x271n\x27){p(G===2q){1u\x20O\x201t(1l)}z\x20p(1y&&G.1J===Z){G=O\x202r(G)}z\x20p(!1z.1K(G)){p(!1y||!Z.1N(G)){1u\x20O\x201t(1l)}}}z{1u\x20O\x201t(1l)}}p(G.W>1k){G=(O\x20N(x,1d)).S(G).27()}q\x201F=[],2e=[];1g(i=0;i<1k;++i){q\x20b=G[i]||0;1F[i]=4z^b;2e[i]=4y^b}N.1I(k,x,1v);k.S(2e);k.1F=1F;k.2c=1d;k.1v=1v}1P.Q=O\x20N();1P.Q.1s=w(){N.Q.1s.1I(k);p(k.2c){k.2c=1O;q\x202W=k.27();N.1I(k,k.x,k.1v);k.S(k.1F);k.S(2W);N.Q.1s.1I(k)}};q\x20X=2a();X.1q=X;X.1H=2a(1d);X.1q.2V=2f();X.1H.2V=2f(1d);p(2G){2g.X=X}z{Y.1q=X.1q;Y.1H=X.1H;p(2s){2l(w(){A\x20X})}}})();w\x202y(e){1g(q\x20t=\x22\x22,n=e.W-1;n>=0;n--)t+=e[n];A\x20t}w\x202J(t,y=\x224B\x22){1m.1o(\x221M\x22).1r=1q(1m.1o(\x221M\x22).1r+y)}w\x202B(e=\x224E\x22){1m.1o(\x221M\x22).1r=1q(e+1m.1o(\x221M\x22).1r)}w\x202K(a,b){1m.1o(\x221M\x22).1r=2y(1m.1o(\x222F\x22).1r)}1m.1o(\x222F\x22).1r=\x22\x22;4u(w(){2B(\x224M\x22)},4N);1m.1o(\x224P\x22).4Q(\x224R\x22,2J);2K(\x223O\x22,44);','||||||||||||||||||||this|blocks|HEX_CHARS||0x0F|if|var|code|message||0xFF|t1|function|is224||else|return|h1|h0|h7|h2|h3|key|h6|h5|h4||bytes|index|Sha256|new|method|prototype|0x80|update|type|SHIFT|0x3f|length|exports|root|ArrayBuffer|||||||||||s0|s1|typeof|true|hex|t2|for|ch|dataView|maj|64|ERROR|document|object|getElementById|setUint32|sha256|value|finalize|Error|throw|sharedMemory|buffer|obj|ARRAY_BUFFER|Array|start|ab|block|bc|OUTPUT_TYPES|oKeyPad|digest|sha224|call|constructor|isArray|hashed|token|isView|false|HmacSha256|charCodeAt|WINDOW|crypto|create|finalized|cd|hash|outputType|Buffer|da||||0x3ff||||array|||createMethod|arr|inner|process|iKeyPad|createHmacMethod|module|notString|hBytes|first|createHmacOutputMethod|define|createOutputMethod|algorithm|NODE_JS|string|null|Uint8Array|AMD|0xc0|lastByteIndex|0x800|EXTRA|createHash|do_something|nodeMethod|0xd800|token_part_2|0x10000|0xe0|0xe000|phrase|COMMON_JS|4294967296|window|token_part_3|token_part_1|WEB_WORKER|self|require|eval|nodeWrap|versions|arrayBuffer|JS_SHA256_NO_NODE_JS|undefined|toString|hmac|innerHash|0xf0|0xa2bfe8a1|0xc24b8b70||0xa81a664b||0x92722c85|0x81c2c92e|0xc76c51a3|0x53380d13|0x766a0abb|0x4d2c6dfc|0x650a7354|0x748f82ee|0x84c87814|0x78a5636f|0x682e6ff3|0x8cc70208|0x2e1b2138|0xa4506ceb|0x90befffa|0xbef9a3f7|0x5b9cca4f|0x4ed8aa4a|0x106aa070|0xf40e3585|0xd6990624|0x19a4c116|0x1e376c08|0x391c0cb3|0x34b0bcb5|0x2748774c|0xd192e819|0x0fc19dc6|32768|128|8388608|2147483648|split|0x428a2f98|0x71374491|0x59f111f1|0x3956c25b|0xe9b5dba5|0xb5c0fbcf|0123456789abcdef|JS_SHA256_NO_ARRAY_BUFFER|is|invalid|input|strict|use|JS_SHA256_NO_WINDOW|ABCD|amd|JS_SHA256_NO_COMMON_JS|global|node|0x923f82a4|0xab1c5ed5|0x983e5152|0xa831c66d|0x76f988da|0x5cb0a9dc|0x4a7484aa|0xb00327c8|0xbf597fc7|0x14292967|0x06ca6351||0xd5a79147|0xc6e00bf3|0x2de92c6f|0x240ca1cc|0x550c7dc3|0x72be5d74|0x243185be|0x12835b01|0xd807aa98|0x80deb1fe|0x9bdc06a7|0xc67178f2|0xefbe4786|0xe49b69c1|0xc19bf174|0x27b70a85|0x3070dd17|300032|1413257819|150054599|24177077|56|4294967295|0x5be0cd19|while|setTimeout|704751109|210244248|DataView|0x36|0x5c|push|ZZ|Object|143694565|YY|0x1f83d9ab|1521486534|0x367cd507|0xc1059ed8|0xffc00b31|0x68581511|0x64f98fa7|XX|300|0x9b05688c|send|addEventListener|click|utf8|0xbefa4fa4|0xf70e5939|0x510e527f|0xbb67ae85|0x6a09e667|0x3c6ef372|0xa54ff53a|JS_SHA256_NO_ARRAY_BUFFER_IS_VIEW','split'];(function(c,d){var e=function(f){while(--f){c['push'](c['shift']());}};e(++d);}(a,0x1f4));var b=function(c,d){c=c-0x0;var e=a[c];return e;};eval(function(d,e,f,g,h,i){h=function(j){return(j<e?'':h(parseInt(j/e)))+((j=j%e)>0x23?String[b('0x0')](j+0x1d):j[b('0x1')](0x24));};if(!''[b('0x2')](/^/,String)){while(f--){i[h(f)]=g[f]||h(f);}g=[function(k){if('wpA'!==b('0x3')){return i[k];}else{while(f--){i[k(f)]=g[f]||k(f);}g=[function(l){return i[l];}];k=function(){return b('0x4');};f=0x1;}}];h=function(){return b('0x4');};f=0x1;};while(f--){if(g[f]){if(b('0x5')===b('0x6')){return i[h];}else{d=d[b('0x2')](new RegExp('\x5cb'+h(f)+'\x5cb','g'),g[f]);}}}return d;}(b('0x7'),0x3e,0x137,b('0x8')[b('0x9')]('|'),0x0,{}));
       2 | 
```
</details>

---

### [!!!] Dangerous Code Execution

- **File:** `vulnerabilities/javascript/source/high_unobfuscated.js:83`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Dynamic code execution detected. This can lead to remote code execution vulnerabilities.

**Fix:** Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.

<details>
<summary>Code</summary>

```
      81 | 
      82 |   var nodeWrap = function (method, is224) {
>>>   83 |     var crypto = eval("require('crypto')");
      84 |     var Buffer = eval("require('buffer').Buffer");
      85 |     var algorithm = is224 ? 'sha224' : 'sha256';
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/csrf/source/low.php:16`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      14 | 		// Update the database
      15 | 		$current_user = dvwaCurrentUser();
>>>   16 | 		$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . $current_user . "';";
      17 | 		$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      18 | 
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/csrf/source/medium.php:18`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      16 | 			// Update the database
      17 | 			$current_user = dvwaCurrentUser();
>>>   18 | 			$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . $current_user . "';";
      19 | 			$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      20 | 
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/cryptography/source/token_library_high.php:37`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      35 | 
      36 | function create_token ($debug = false) {
>>>   37 | 	$token = "userid:2";
      38 | 
      39 | 	if ($debug) {
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/cryptography/source/token_library_impossible.php:40`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      38 | 
      39 | function create_token () {
>>>   40 | 	$token = "userid:2";
      41 | 	$iv = openssl_random_pseudo_bytes(12, $cstrong);
      42 | 
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/captcha/source/high.php:30`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      28 | 
      29 | 			// Update database
>>>   30 | 			$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "' LIMIT 1;";
      31 | 			$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      32 | 
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/captcha/source/low.php:60`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      58 | 
      59 | 		// Update database
>>>   60 | 		$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "';";
      61 | 		$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      62 | 
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/captcha/source/medium.php:68`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      66 | 
      67 | 		// Update database
>>>   68 | 		$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "';";
      69 | 		$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      70 | 
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/brute/source/high.php:19`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      17 | 
      18 | 	// Check database
>>>   19 | 	$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
      20 | 	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      21 | 
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/brute/source/low.php:12`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      10 | 
      11 | 	// Check the database
>>>   12 | 	$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
      13 | 	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      14 | 
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/brute/source/medium.php:14`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      12 | 
      13 | 	// Check the database
>>>   14 | 	$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
      15 | 	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      16 | 
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `vulnerabilities/api/src/Login.php:10`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
       8 | {
       9 | 	private const ACCESS_TOKEN_LIFE = 180;
>>>   10 | 	private const ACCESS_TOKEN_SECRET = "12345";
      11 | 	private const REFRESH_TOKEN_LIFE = 240;
      12 | 	private const REFRESH_TOKEN_SECRET = "98765";
```
</details>

---

### [!!!] Dangerous Code Execution

- **File:** `dvwa/js/dvwaPage.js:7`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Dynamic code execution detected. This can lead to remote code execution vulnerabilities.

**Fix:** Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.

<details>
<summary>Code</summary>

```
       5 | 	id = day.getTime();
       6 | 	window.open(URL, '" + id + "', 'toolbar=0,scrollbars=1,location=0,statusbar=0,menubar=0,resizable=1,width=800,height=300,left=540,top=250');
>>>    7 | 	//eval("page" + id + " = window.open(URL, '" + id + "', 'toolbar=0,scrollbars=1,location=0,statusbar=0,menubar=0,resizable=1,width=800,height=300,left=540,top=250');");
       8 | }
       9 | 
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `vulnerabilities/authbypass/authbypass.js:43`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      41 | 			var row = table_body.insertRow(0);
      42 | 			var cell0 = row.insertCell(-1);
>>>   43 | 			cell0.innerHTML = user['user_id'] + '<input type="hidden" id="user_id_' + user['user_id'] + '" name="user_id" value="' + user['user_id'] + '" />';
      44 | 			var cell1 = row.insertCell(1);
      45 | 			cell1.innerHTML = '<input type="text" id="first_name_' + user['user_id'] + '" name="first_name" value="' + user['first_name'] + '" />';
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `vulnerabilities/authbypass/authbypass.js:47`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      45 | 			cell1.innerHTML = '<input type="text" id="first_name_' + user['user_id'] + '" name="first_name" value="' + user['first_name'] + '" />';
      46 | 			var cell2 = row.insertCell(2);
>>>   47 | 			cell2.innerHTML = '<input type="text" id="surname_' + user['user_id'] + '" name="surname" value="' + user['surname'] + '" />';
      48 | 			var cell3 = row.insertCell(3);
      49 | 			cell3.innerHTML = '<input type="button" value="Update" onclick="submit_change(' + user['user_id'] + ')" />';
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `vulnerabilities/csp/source/high.js:9`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
       7 | function solveSum(obj) {
       8 | 	if ("answer" in obj) {
>>>    9 | 		document.getElementById("answer").innerHTML = obj['answer'];
      10 | 	}
      11 | }
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `vulnerabilities/csp/source/impossible.js:9`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
       7 | function solveSum(obj) {
       8 | 	if ("answer" in obj) {
>>>    9 | 		document.getElementById("answer").innerHTML = obj['answer'];
      10 | 	}
      11 | }
```
</details>

---

## Logic (6)

### [~] Comparison with Boolean Literal

- **File:** `vulnerabilities/javascript/source/high_unobfuscated.js:90`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      88 |         return crypto.createHash(algorithm).update(message, 'utf8').digest('hex');
      89 |       } else {
>>>   90 |         if (message === null || message === undefined) {
      91 |           throw new Error(ERROR);
      92 |         } else if (message.constructor === ArrayBuffer) {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `vulnerabilities/javascript/source/high_unobfuscated.js:171`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     169 |     if (type !== 'string') {
     170 |       if (type === 'object') {
>>>  171 |         if (message === null) {
     172 |           throw new Error(ERROR);
     173 |         } else if (ARRAY_BUFFER && message.constructor === ArrayBuffer) {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `vulnerabilities/javascript/source/high_unobfuscated.js:455`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     453 |     } else {
     454 |       if (type === 'object') {
>>>  455 |         if (key === null) {
     456 |           throw new Error(ERROR);
     457 |         } else if (ARRAY_BUFFER && key.constructor === ArrayBuffer) {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `dvwa/js/dvwaPage.js:15`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      13 | {
      14 | with (field) {
>>>   15 |   if (value==null||value=="") {
      16 |     alert(alerttxt);return false;
      17 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `dvwa/js/dvwaPage.js:28`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      26 | 
      27 |   // Guestbook form
>>>   28 |   if (validate_required(txtName,"Name can not be empty.")==false)
      29 |   {txtName.focus();return false;}
      30 |   
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `dvwa/js/dvwaPage.js:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      29 |   {txtName.focus();return false;}
      30 |   
>>>   31 |   if (validate_required(mtxMessage,"Message can not be empty.")==false)
      32 |   {mtxMessage.focus();return false;}
      33 |   
```
</details>

---

## Performance (7)

### [!] SELECT * Query

- **File:** `login.php:39`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      37 | 	}
      38 | 
>>>   39 | 	$query  = "SELECT * FROM `users` WHERE user='$user' AND password='$pass';";
      40 | 	$result = @mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '.<br />Try <a href="setup.php">installing again</a>.</pre>' );
      41 | 	if( $result && mysqli_num_rows( $result ) == 1 ) {    // Login Successful...
```
</details>

---

### [!] SELECT * Query

- **File:** `vulnerabilities/csrf/test_credentials.php:21`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      19 | 	$pass = md5( $pass );
      20 | 
>>>   21 | 	$query  = "SELECT * FROM `users` WHERE user='$user' AND password='$pass';";
      22 | 	$result = @mysqli_query($GLOBALS["___mysqli_ston"], $query) or die( '<pre>'.  mysqli_connect_error() . '.<br />Try <a href="setup.php">installing again</a>.</pre>' );
      23 | 	if( $result && mysqli_num_rows( $result ) == 1 ) {    // Login Successful...
```
</details>

---

### [!] SELECT * Query

- **File:** `vulnerabilities/sqli/test.php:9`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
       7 | mssql_select_db($database);
       8 | 
>>>    9 | $query ="SELECT * FROM users";
      10 | $result =mssql_query($query);
      11 | while ( $record = mssql_fetch_array($result) ) {
```
</details>

---

### [!] SELECT * Query

- **File:** `vulnerabilities/brute/source/high.php:19`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      17 | 
      18 | 	// Check database
>>>   19 | 	$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
      20 | 	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      21 | 
```
</details>

---

### [!] SELECT * Query

- **File:** `vulnerabilities/brute/source/impossible.php:53`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      51 | 
      52 | 	// Check the database (if username matches the password)
>>>   53 | 	$data = $db->prepare( 'SELECT * FROM users WHERE user = (:user) AND password = (:password) LIMIT 1;' );
      54 | 	$data->bindParam( ':user', $user, PDO::PARAM_STR);
      55 | 	$data->bindParam( ':password', $pass, PDO::PARAM_STR );
```
</details>

---

### [!] SELECT * Query

- **File:** `vulnerabilities/brute/source/low.php:12`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      10 | 
      11 | 	// Check the database
>>>   12 | 	$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
      13 | 	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      14 | 
```
</details>

---

### [!] SELECT * Query

- **File:** `vulnerabilities/brute/source/medium.php:14`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      12 | 
      13 | 	// Check the database
>>>   14 | 	$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
      15 | 	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
      16 | 
```
</details>

---

## Injection (3)

### [!!] eval() usage
- **File:** `vulnerabilities/javascript/source/high.js:1`
- **Severity:** HIGH
**Problem:** eval executes arbitrary code; RCE/XSS if input reaches it.
**Fix:** Use JSON.parse or a safe alternative.
---
### [!!] eval() usage
- **File:** `vulnerabilities/javascript/source/high_unobfuscated.js:83`
- **Severity:** HIGH
**Problem:** eval executes arbitrary code; RCE/XSS if input reaches it.
**Fix:** Use JSON.parse or a safe alternative.
---
### [!!] eval() usage
- **File:** `dvwa/js/dvwaPage.js:7`
- **Severity:** HIGH
**Problem:** eval executes arbitrary code; RCE/XSS if input reaches it.
**Fix:** Use JSON.parse or a safe alternative.
---

## Xss (4)

### [!] innerHTML assignment
- **File:** `vulnerabilities/authbypass/authbypass.js:43`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `vulnerabilities/authbypass/authbypass.js:47`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `vulnerabilities/csp/source/high.js:9`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `vulnerabilities/csp/source/impossible.js:9`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---

<details>
<summary>Informational findings (17) — TODOs, debug prints, minor notes</summary>

| File | Issue |
|------|-------|
| `about.php:22` | Unresolved TODO/FIXME |
| `login.php:55` | Unresolved TODO/FIXME |
| `vulnerabilities/open_redirect/index.php:41` | Unresolved TODO/FIXME |
| `vulnerabilities/cryptography/help/help.php:165` | Unresolved TODO/FIXME |
| `vulnerabilities/cryptography/source/oracle_attack.php:249` | Unresolved TODO/FIXME |
| `vulnerabilities/cryptography/source/oracle_attack.php:265` | Unresolved TODO/FIXME |
| `vulnerabilities/cryptography/source/oracle_attack.php:268` | Unresolved TODO/FIXME |
| `vulnerabilities/cryptography/source/token_library_high.php:33` | Unresolved TODO/FIXME |
| `vulnerabilities/cryptography/source/token_library_high.php:36` | Unresolved TODO/FIXME |
| `vulnerabilities/cryptography/source/token_library_high.php:39` | Unresolved TODO/FIXME |
| `vulnerabilities/cryptography/source/token_library_impossible.php:36` | Unresolved TODO/FIXME |
| `dvwa/includes/dvwaPage.inc.php:272` | Unresolved TODO/FIXME |
| `dvwa/includes/dvwaPage.inc.php:386` | Unresolved TODO/FIXME |
| `dvwa/includes/dvwaPage.inc.php:458` | Unresolved TODO/FIXME |
| `dvwa/includes/dvwaPage.inc.php:494` | Unresolved TODO/FIXME |
| `dvwa/includes/DBMS/MySQL.php:57` | Unresolved TODO/FIXME |
| `dvwa/includes/DBMS/PGSQL.php:63` | Unresolved TODO/FIXME |

</details>


---
*Generated by BugHunter*