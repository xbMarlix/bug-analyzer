# BugHunter Report: juice-shop

**Generated:** 2026-09-15 15:44:59
**Project:** `/tmp/juice-shop`
**Analyzers:** static

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 676 |
| Total lines | 60,971 |
| Bugs found | 247 |
| !!! Critical | 13 |
| !! High | 13 |
| ! Medium | 45 |
| ~ Low | 116 |
| i Info | 60 |

## Top Findings (10)

| Severity | File | Issue |
|----------|------|-------|
| CRITICAL | `routes/b2bOrder.ts:23` | Dangerous Code Execution |
| CRITICAL | `routes/captcha.ts:22` | Dangerous Code Execution |
| CRITICAL | `routes/login.ts:34` | Hardcoded Secret |
| CRITICAL | `routes/userProfile.ts:65` | Dangerous Code Execution |
| CRITICAL | `frontend/src/app/login/login.component.ts:63` | Hardcoded Secret |
| CRITICAL | `frontend/src/app/register/register.component.spec.ts:137` | Hardcoded Secret |
| CRITICAL | `data/static/codefixes/loginAdminChallenge_1.ts:18` | Hardcoded Secret |
| CRITICAL | `data/static/codefixes/loginAdminChallenge_2.ts:15` | Hardcoded Secret |
| CRITICAL | `data/static/codefixes/loginBenderChallenge_1.ts:18` | Hardcoded Secret |
| CRITICAL | `data/static/codefixes/loginBenderChallenge_3.ts:15` | Hardcoded Secret |

### Languages Detected

- **typescript**: 482 files
- **scss**: 83 files
- **html**: 82 files
- **solidity**: 17 files
- **javascript**: 8 files
- **css**: 3 files
- **bash**: 1 files

## Security (26)

### [!!!] Dangerous Code Execution

- **File:** `routes/b2bOrder.ts:23`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Dynamic code execution detected. This can lead to remote code execution vulnerabilities.

**Fix:** Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.

<details>
<summary>Code</summary>

```
      21 |         const sandbox = { safeEval, orderLinesData }
      22 |         vm.createContext(sandbox)
>>>   23 |         vm.runInContext('safeEval(orderLinesData)', sandbox, { timeout: 2000 })
      24 |         res.json({ cid: body.cid, orderNo: uniqueOrderNumber(), paymentDue: dateTwoWeeksFromNow() })
      25 |       } catch (err) {
```
</details>

---

### [!!!] Dangerous Code Execution

- **File:** `routes/captcha.ts:22`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Dynamic code execution detected. This can lead to remote code execution vulnerabilities.

**Fix:** Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.

<details>
<summary>Code</summary>

```
      20 | 
      21 |     const expression = firstTerm.toString() + firstOperator + secondTerm.toString() + secondOperator + thirdTerm.toString()
>>>   22 |     const answer = eval(expression).toString() // eslint-disable-line no-eval
      23 | 
      24 |     const captcha = {
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `routes/login.ts:34`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      32 |   return (req: Request, res: Response, next: NextFunction) => {
      33 |     verifyPreLoginChallenges(req) // vuln-code-snippet hide-line
>>>   34 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: UserModel, plain: true }) // vuln-code-snippet vuln-line loginAdminChallenge loginBenderChallenge loginJimChallenge
      35 |       .then((authenticatedUser) => { // vuln-code-snippet neutral-line loginAdminChallenge loginBenderChallenge loginJimChallenge
      36 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!!!] Dangerous Code Execution

- **File:** `routes/userProfile.ts:65`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Dynamic code execution detected. This can lead to remote code execution vulnerabilities.

**Fix:** Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.

<details>
<summary>Code</summary>

```
      63 |             throw new Error('Username is null')
      64 |           }
>>>   65 |           username = eval(code) // eslint-disable-line no-eval
      66 |         } catch (err) {
      67 |           username = '\\' + username
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `frontend/src/app/login/login.component.ts:63`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      61 |   public redirectUri = ''
      62 |   public testingUsername = 'testing@juice-sh.op'
>>>   63 |   public testingPassword = 'IamUsedForTesting'
      64 | 
      65 |   ngOnInit (): void {
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `frontend/src/app/register/register.component.spec.ts:137`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
     135 | 
     136 |     it('password and repeat password should be the same', () => {
>>>  137 |         const password = 'aaaaa'
     138 |         const passwordRepeat = 'aaaaa'
     139 |         component.passwordControl.setValue(password)
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `data/static/codefixes/loginAdminChallenge_1.ts:18`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      16 |       res.status(451).send(res.__('SQL Injection detected.'))
      17 |     }
>>>   18 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: true })
      19 |       .then((authenticatedUser) => {
      20 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `data/static/codefixes/loginAdminChallenge_2.ts:15`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`,
      16 |       { bind: [ req.body.email ], model: models.User, plain: true })
      17 |       .then((authenticatedUser) => {
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `data/static/codefixes/loginBenderChallenge_1.ts:18`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      16 |       res.status(451).send(res.__('SQL Injection detected.'))
      17 |     }
>>>   18 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: true })
      19 |       .then((authenticatedUser) => {
      20 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `data/static/codefixes/loginBenderChallenge_3.ts:15`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = :mail AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`,
      16 |       { replacements: { mail: req.body.email }, model: models.User, plain: true })
      17 |       .then((authenticatedUser) => {
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `data/static/codefixes/loginBenderChallenge_4.ts:15`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: false })
      16 |       .then((authenticatedUser) => {
      17 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `data/static/codefixes/loginJimChallenge_2.ts:15`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: false })
      16 |       .then((authenticatedUser) => {
      17 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!!!] Hardcoded Secret

- **File:** `data/static/codefixes/loginJimChallenge_4.ts:18`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** A secret or password appears to be hardcoded in source code.

**Fix:** Use environment variables or a secrets manager instead of hardcoding.

<details>
<summary>Code</summary>

```
      16 |       res.status(451).send(res.__('SQL Injection detected.'))
      17 |     }
>>>   18 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: true })
      19 |       .then((authenticatedUser) => {
      20 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/hacking-instructor/index.ts:126`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     124 | 
     125 |   const textBox = createElement('span', { flexGrow: '2' })
>>>  126 |   textBox.innerHTML = snarkdown(hint.text)
     127 | 
     128 |   const cancelButtonStyles = {
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/hacking-instructor/index.ts:142`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     140 | 
     141 |   const cancelButton = createElement('button', cancelButtonStyles, { id: 'cancelButton', title: 'Cancel the tutorial' })
>>>  142 |   cancelButton.innerHTML = '<div>&times;</div>'
     143 | 
     144 |   elem.appendChild(picture)
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:138`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     136 |       )
     137 | 
>>>  138 |       if (element && element.innerHTML === value) {
     139 |         break
     140 |       }
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/assets/private/dat.gui.min.js:1`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
>>>    1 | var dat=dat||{};dat.gui=dat.gui||{};dat.utils=dat.utils||{};dat.controllers=dat.controllers||{};dat.dom=dat.dom||{};dat.color=dat.color||{};dat.utils.css=function(){return{load:function(e,a){a=a||document;var b=a.createElement("link");b.type="text/css";b.rel="stylesheet";b.href=e;a.getElementsByTagName("head")[0].appendChild(b)},inject:function(e,a){a=a||document;var b=document.createElement("style");b.type="text/css";b.innerHTML=e;a.getElementsByTagName("head")[0].appendChild(b)}}}();
       2 | dat.utils.common=function(){var e=Array.prototype.forEach,a=Array.prototype.slice;return{BREAK:{},extend:function(b){this.each(a.call(arguments,1),function(a){for(var f in a)this.isUndefined(a[f])||(b[f]=a[f])},this);return b},defaults:function(b){this.each(a.call(arguments,1),function(a){for(var f in a)this.isUndefined(b[f])&&(b[f]=a[f])},this);return b},compose:function(){var b=a.call(arguments);return function(){for(var d=a.call(arguments),f=b.length-1;0<=f;f--)d=[b[f].apply(this,d)];return d[0]}},
       3 |     each:function(a,d,f){if(e&&a.forEach===e)a.forEach(d,f);else if(a.length===a.length+0)for(var c=0,p=a.length;c<p&&!(c in a&&d.call(f,a[c],c)===this.BREAK);c++);else for(c in a)if(d.call(f,a[c],c)===this.BREAK)break},defer:function(a){setTimeout(a,0)},toArray:function(b){return b.toArray?b.toArray():a.call(b)},isUndefined:function(a){return void 0===a},isNull:function(a){return null===a},isNaN:function(a){return a!==a},isArray:Array.isArray||function(a){return a.constructor===Array},isObject:function(a){return a===
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/assets/private/dat.gui.min.js:13`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      11 |         e&&(b.splice(e,1),a.className=b.join(" "))}}else a.className=void 0;return f},hasClass:function(a,d){return RegExp("(?:^|\\s+)"+d+"(?:\\s+|$)").test(a.className)||!1},getWidth:function(c){c=getComputedStyle(c);return a(c["border-left-width"])+a(c["border-right-width"])+a(c["padding-left"])+a(c["padding-right"])+a(c.width)},getHeight:function(c){c=getComputedStyle(c);return a(c["border-top-width"])+a(c["border-bottom-width"])+a(c["padding-top"])+a(c["padding-bottom"])+a(c.height)},getOffset:function(a){var d=
      12 |     {left:0,top:0};if(a.offsetParent){do d.left+=a.offsetLeft,d.top+=a.offsetTop;while(a=a.offsetParent)}return d},isActive:function(a){return a===document.activeElement&&(a.type||a.href)}};return f}(dat.utils.common);
>>>   13 | dat.controllers.OptionController=function(e,a,b){var d=function(f,c,e){d.superclass.call(this,f,c);var k=this;this.__select=document.createElement("select");if(b.isArray(e)){var l={};b.each(e,function(a){l[a]=a});e=l}b.each(e,function(a,c){var d=document.createElement("option");d.innerHTML=c;d.setAttribute("value",a);k.__select.appendChild(d)});this.updateDisplay();a.bind(this.__select,"change",function(){k.setValue(this.options[this.selectedIndex].value)});this.domElement.appendChild(this.__select)};
      14 |     d.superclass=e;b.extend(d.prototype,e.prototype,{setValue:function(a){a=d.superclass.prototype.setValue.call(this,a);this.__onFinishChange&&this.__onFinishChange.call(this,this.getValue());return a},updateDisplay:function(){this.__select.value=this.getValue();return d.superclass.prototype.updateDisplay.call(this)}});return d}(dat.controllers.Controller,dat.dom.dom,dat.utils.common);
      15 | dat.controllers.NumberController=function(e,a){var b=function(d,f,c){b.superclass.call(this,d,f);c=c||{};this.__min=c.min;this.__max=c.max;this.__step=c.step;a.isUndefined(this.__step)?this.__impliedStep=0==this.initialValue?1:Math.pow(10,Math.floor(Math.log(this.initialValue)/Math.LN10))/10:this.__impliedStep=this.__step;d=this.__impliedStep;d=d.toString();d=-1<d.indexOf(".")?d.length-d.indexOf(".")-1:0;this.__precision=d};b.superclass=e;a.extend(b.prototype,e.prototype,{setValue:function(a){void 0!==
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/assets/private/dat.gui.min.js:23`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      21 |     document.createElement("div");this.__foreground=document.createElement("div");a.bind(this.__background,"mousedown",function(c){a.bind(window,"mousemove",y);a.bind(window,"mouseup",g);y(c)});a.addClass(this.__background,"slider");a.addClass(this.__foreground,"slider-fg");this.updateDisplay();this.__background.appendChild(this.__foreground);this.domElement.appendChild(this.__background)};p.superclass=e;p.useDefaultStyles=function(){b.inject(f)};d.extend(p.prototype,e.prototype,{updateDisplay:function(){var a=
      22 |     (this.getValue()-this.__min)/(this.__max-this.__min);this.__foreground.style.width=100*a+"%";return p.superclass.prototype.updateDisplay.call(this)}});return p}(dat.controllers.NumberController,dat.dom.dom,dat.utils.css,dat.utils.common,"/**\n * dat-gui JavaScript Controller Library\n * http://code.google.com/p/dat-gui\n *\n * Copyright 2011 Data Arts Team, Google Creative Lab\n *\n * Licensed under the Apache License, Version 2.0 (the \"License\");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n * http://www.apache.org/licenses/LICENSE-2.0\n */\n\n.slider {\n  box-shadow: inset 0 2px 4px rgba(0,0,0,0.15);\n  height: 1em;\n  border-radius: 1em;\n  background-color: #eee;\n  padding: 0 0.5em;\n  overflow: hidden;\n}\n\n.slider-fg {\n  padding: 1px 0 2px 0;\n  background-color: #aaa;\n  height: 1em;\n  margin-left: -0.5em;\n  padding-right: 0.5em;\n  border-radius: 1em 0 0 1em;\n}\n\n.slider-fg:after {\n  display: inline-block;\n  border-radius: 1em;\n  background-color: #fff;\n  border:  1px solid #aaa;\n  content: '';\n  float: right;\n  margin-right: -1em;\n  margin-top: -1px;\n  height: 0.9em;\n  width: 0.9em;\n}");
>>>   23 | dat.controllers.FunctionController=function(e,a,b){var d=function(b,c,e){d.superclass.call(this,b,c);var k=this;this.__button=document.createElement("div");this.__button.innerHTML=void 0===e?"Fire":e;a.bind(this.__button,"click",function(a){a.preventDefault();k.fire();return!1});a.addClass(this.__button,"button");this.domElement.appendChild(this.__button)};d.superclass=e;b.extend(d.prototype,e.prototype,{fire:function(){this.__onChange&&this.__onChange.call(this);this.__onFinishChange&&this.__onFinishChange.call(this,
      24 |     this.getValue());this.getValue().call(this.object)}});return d}(dat.controllers.Controller,dat.dom.dom,dat.utils.common);
      25 | dat.controllers.BooleanController=function(e,a,b){var d=function(b,c){d.superclass.call(this,b,c);var e=this;this.__prev=this.getValue();this.__checkbox=document.createElement("input");this.__checkbox.setAttribute("type","checkbox");a.bind(this.__checkbox,"change",function(){e.setValue(!e.__prev)},!1);this.domElement.appendChild(this.__checkbox);this.updateDisplay()};d.superclass=e;b.extend(d.prototype,e.prototype,{setValue:function(a){a=d.superclass.prototype.setValue.call(this,a);this.__onFinishChange&&
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/assets/private/dat.gui.min.js:33`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      31 |     a.isNumber(c.g)&&a.isNumber(c.b)?{space:"RGB",r:c.r,g:c.g,b:c.b}:!1},write:function(a){return{r:a.r,g:a.g,b:a.b}}},HSVA_OBJ:{read:function(c){return a.isNumber(c.h)&&a.isNumber(c.s)&&a.isNumber(c.v)&&a.isNumber(c.a)?{space:"HSV",h:c.h,s:c.s,v:c.v,a:c.a}:!1},write:function(a){return{h:a.h,s:a.s,v:a.v,a:a.a}}},HSV_OBJ:{read:function(d){return a.isNumber(d.h)&&a.isNumber(d.s)&&a.isNumber(d.v)?{space:"HSV",h:d.h,s:d.s,v:d.v}:!1},write:function(a){return{h:a.h,s:a.s,v:a.v}}}}}];return function(){d=!1;
      32 |     var c=1<arguments.length?a.toArray(arguments):arguments[0];a.each(f,function(e){if(e.litmus(c))return a.each(e.conversions,function(e,f){b=e.read(c);if(!1===d&&!1!==b)return d=b,b.conversionName=f,b.conversion=e,a.BREAK}),a.BREAK});return d}}(dat.color.toString,dat.utils.common);
>>>   33 | dat.GUI=dat.gui.GUI=function(e,a,b,d,f,c,p,k,l,q,n,r,y,g,h){function t(a,c,b,e){if(void 0===c[b])throw Error("Object "+c+' has no property "'+b+'"');e.color?c=new n(c,b):(c=[c,b].concat(e.factoryArgs),c=d.apply(a,c));e.before instanceof f&&(e.before=e.before.__li);v(a,c);g.addClass(c.domElement,"c");b=document.createElement("span");g.addClass(b,"property-name");b.innerHTML=c.property;var q=document.createElement("div");q.appendChild(b);q.appendChild(c.domElement);e=u(a,q,e.before);g.addClass(e,m.CLASS_CONTROLLER_ROW);
      34 |     g.addClass(e,typeof c.getValue());s(a,e,c);a.__controllers.push(c);return c}function u(a,d,c){var b=document.createElement("li");d&&b.appendChild(d);c?a.__ul.insertBefore(b,params.before):a.__ul.appendChild(b);a.onResize();return b}function s(a,d,b){b.__li=d;b.__gui=a;h.extend(b,{options:function(d){if(1<arguments.length)return b.remove(),t(a,b.object,b.property,{before:b.__li.nextElementSibling,factoryArgs:[h.toArray(arguments)]});if(h.isArray(d)||h.isObject(d))return b.remove(),t(a,b.object,b.property,
      35 |     {before:b.__li.nextElementSibling,factoryArgs:[d]})},name:function(a){b.__li.firstElementChild.firstElementChild.innerHTML=a;return b},listen:function(){b.__gui.listen(b);return b},remove:function(){b.__gui.remove(b);return b}});if(b instanceof l){var e=new k(b.object,b.property,{min:b.__min,max:b.__max,step:b.__step});h.each(["updateDisplay","onChange","onFinishChange"],function(a){var d=b[a],J=e[a];b[a]=e[a]=function(){var a=Array.prototype.slice.call(arguments);d.apply(b,a);return J.apply(e,a)}});
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/assets/private/dat.gui.min.js:39`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      37 |     b instanceof p?(g.bind(d,"click",function(){g.fakeEvent(b.__button,"click")}),g.bind(d,"mouseover",function(){g.addClass(b.__button,"hover")}),g.bind(d,"mouseout",function(){g.removeClass(b.__button,"hover")})):b instanceof n&&(g.addClass(d,"color"),b.updateDisplay=h.compose(function(a){d.style.borderLeftColor=b.__color.toString();return a},b.updateDisplay),b.updateDisplay());b.setValue=h.compose(function(d){a.getRoot().__preset_select&&b.isModified()&&D(a.getRoot(),!0);return d},b.setValue)}function v(a,
      38 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 d){var b=a.getRoot(),c=b.__rememberedObjects.indexOf(d.object);if(-1!=c){var e=b.__rememberedObjectIndecesToControllers[c];void 0===e&&(e={},b.__rememberedObjectIndecesToControllers[c]=e);e[d.property]=d;if(b.load&&b.load.remembered){b=b.load.remembered;if(b[a.preset])b=b[a.preset];else if(b[z])b=b[z];else return;b[c]&&void 0!==b[c][d.property]&&(c=b[c][d.property],d.initialValue=c,d.setValue(c))}}}function K(a){var b=a.__save_row=document.createElement("li");g.addClass(a.domElement,"has-save");a.__ul.insertBefore(b,
>>>   39 |     a.__ul.firstChild);g.addClass(b,"save-row");var d=document.createElement("span");d.innerHTML="&nbsp;";g.addClass(d,"button gears");var c=document.createElement("span");c.innerHTML="Save";g.addClass(c,"button");g.addClass(c,"save");var e=document.createElement("span");e.innerHTML="New";g.addClass(e,"button");g.addClass(e,"save-as");var f=document.createElement("span");f.innerHTML="Revert";g.addClass(f,"button");g.addClass(f,"revert");var q=a.__preset_select=document.createElement("select");a.load&&
      40 |     a.load.remembered?h.each(a.load.remembered,function(b,d){E(a,d,d==a.preset)}):E(a,z,!1);g.bind(q,"change",function(){for(var b=0;b<a.__preset_select.length;b++)a.__preset_select[b].innerHTML=a.__preset_select[b].value;a.preset=this.value});b.appendChild(q);b.appendChild(d);b.appendChild(c);b.appendChild(e);b.appendChild(f);if(w){var b=document.getElementById("dg-save-locally"),n=document.getElementById("dg-local-explain");b.style.display="block";b=document.getElementById("dg-local-storage");"true"===
      41 |     localStorage.getItem(document.location.href+".isLocal")&&b.setAttribute("checked","checked");var k=function(){n.style.display=a.useLocalStorage?"block":"none"};k();g.bind(b,"change",function(){a.useLocalStorage=!a.useLocalStorage;k()})}var r=document.getElementById("dg-new-constructor");g.bind(r,"keydown",function(a){!a.metaKey||67!==a.which&&67!=a.keyCode||A.hide()});g.bind(d,"click",function(){r.innerHTML=JSON.stringify(a.getSaveObject(),void 0,2);A.show();r.focus();r.select()});g.bind(c,"click",
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/assets/private/dat.gui.min.js:44`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      42 |     function(){a.save()});g.bind(e,"click",function(){var b=prompt("Enter a new preset name.");b&&a.saveAs(b)});g.bind(f,"click",function(){a.revert()})}function L(a){function b(f){f.preventDefault();e=f.clientX;g.addClass(a.__closeButton,m.CLASS_DRAG);g.bind(window,"mousemove",d);g.bind(window,"mouseup",c);return!1}function d(b){b.preventDefault();a.width+=e-b.clientX;a.onResize();e=b.clientX;return!1}function c(){g.removeClass(a.__closeButton,m.CLASS_DRAG);g.unbind(window,"mousemove",d);g.unbind(window,
      43 |     "mouseup",c)}a.__resize_handle=document.createElement("div");h.extend(a.__resize_handle.style,{width:"6px",marginLeft:"-3px",height:"200px",cursor:"ew-resize",position:"absolute"});var e;g.bind(a.__resize_handle,"mousedown",b);g.bind(a.__closeButton,"mousedown",b);a.domElement.insertBefore(a.__resize_handle,a.domElement.firstElementChild)}function F(a,b){a.domElement.style.width=b+"px";a.__save_row&&a.autoPlace&&(a.__save_row.style.width=b+"px");a.__closeButton&&(a.__closeButton.style.width=b+"px")}
>>>   44 |     function B(a,b){var d={};h.each(a.__rememberedObjects,function(c,e){var f={};h.each(a.__rememberedObjectIndecesToControllers[e],function(a,d){f[d]=b?a.initialValue:a.getValue()});d[e]=f});return d}function E(a,b,d){var c=document.createElement("option");c.innerHTML=b;c.value=b;a.__preset_select.appendChild(c);d&&(a.__preset_select.selectedIndex=a.__preset_select.length-1)}function D(a,b){var d=a.__preset_select[a.__preset_select.selectedIndex];d.innerHTML=b?d.value+"*":d.value}function G(a){0!=a.length&&
      45 |     r(function(){G(a)});h.each(a,function(a){a.updateDisplay()})}e.inject(b);var z="Default",w;try{w="localStorage"in window&&null!==window.localStorage}catch(M){w=!1}var A,H=!0,x,C=!1,I=[],m=function(a){function b(){localStorage.setItem(document.location.href+".gui",JSON.stringify(c.getSaveObject()))}function d(){var a=c.getRoot();a.width+=1;h.defer(function(){a.width-=1})}var c=this;this.domElement=document.createElement("div");this.__ul=document.createElement("ul");this.domElement.appendChild(this.__ul);
      46 |         g.addClass(this.domElement,"dg");this.__folders={};this.__controllers=[];this.__rememberedObjects=[];this.__rememberedObjectIndecesToControllers=[];this.__listening=[];a=a||{};a=h.defaults(a,{autoPlace:!0,width:m.DEFAULT_WIDTH});a=h.defaults(a,{resizable:a.autoPlace,hideable:a.autoPlace});h.isUndefined(a.load)?a.load={preset:z}:a.preset&&(a.load.preset=a.preset);h.isUndefined(a.parent)&&a.hideable&&I.push(this);a.resizable=h.isUndefined(a.parent)&&a.resizable;a.autoPlace&&h.isUndefined(a.scrollable)&&
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/assets/private/dat.gui.min.js:48`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      46 |         g.addClass(this.domElement,"dg");this.__folders={};this.__controllers=[];this.__rememberedObjects=[];this.__rememberedObjectIndecesToControllers=[];this.__listening=[];a=a||{};a=h.defaults(a,{autoPlace:!0,width:m.DEFAULT_WIDTH});a=h.defaults(a,{resizable:a.autoPlace,hideable:a.autoPlace});h.isUndefined(a.load)?a.load={preset:z}:a.preset&&(a.load.preset=a.preset);h.isUndefined(a.parent)&&a.hideable&&I.push(this);a.resizable=h.isUndefined(a.parent)&&a.resizable;a.autoPlace&&h.isUndefined(a.scrollable)&&
      47 |         (a.scrollable=!0);var e=w&&"true"===localStorage.getItem(document.location.href+".isLocal");Object.defineProperties(this,{parent:{get:function(){return a.parent}},scrollable:{get:function(){return a.scrollable}},autoPlace:{get:function(){return a.autoPlace}},preset:{get:function(){return c.parent?c.getRoot().preset:a.load.preset},set:function(b){c.parent?c.getRoot().preset=b:a.load.preset=b;for(b=0;b<this.__preset_select.length;b++)this.__preset_select[b].value==this.preset&&(this.__preset_select.selectedIndex=
>>>   48 |             b);c.revert()}},width:{get:function(){return a.width},set:function(b){a.width=b;F(c,b)}},name:{get:function(){return a.name},set:function(b){a.name=b;q&&(q.innerHTML=a.name)}},closed:{get:function(){return a.closed},set:function(b){a.closed=b;a.closed?g.addClass(c.__ul,m.CLASS_CLOSED):g.removeClass(c.__ul,m.CLASS_CLOSED);this.onResize();c.__closeButton&&(c.__closeButton.innerHTML=b?m.TEXT_OPEN:m.TEXT_CLOSED)}},load:{get:function(){return a.load}},useLocalStorage:{get:function(){return e},set:function(a){w&&
      49 |         ((e=a)?g.bind(window,"unload",b):g.unbind(window,"unload",b),localStorage.setItem(document.location.href+".isLocal",a))}}});if(h.isUndefined(a.parent)){a.closed=!1;g.addClass(this.domElement,m.CLASS_MAIN);g.makeSelectable(this.domElement,!1);if(w&&e){c.useLocalStorage=!0;var f=localStorage.getItem(document.location.href+".gui");f&&(a.load=JSON.parse(f))}this.__closeButton=document.createElement("div");this.__closeButton.innerHTML=m.TEXT_CLOSED;g.addClass(this.__closeButton,m.CLASS_CLOSE_BUTTON);this.domElement.appendChild(this.__closeButton);
      50 |             g.bind(this.__closeButton,"click",function(){c.closed=!c.closed})}else{void 0===a.closed&&(a.closed=!0);var q=document.createTextNode(a.name);g.addClass(q,"controller-name");f=u(c,q);g.addClass(this.__ul,m.CLASS_CLOSED);g.addClass(f,"title");g.bind(f,"click",function(a){a.preventDefault();c.closed=!c.closed;return!1});a.closed||(this.closed=!1)}a.autoPlace&&(h.isUndefined(a.parent)&&(H&&(x=document.createElement("div"),g.addClass(x,"dg"),g.addClass(x,m.CLASS_AUTO_PLACE_CONTAINER),document.body.appendChild(x),
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/assets/private/dat.gui.min.js:55`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      53 |         2)})},addColor:function(a,b){return t(this,a,b,{color:!0})},remove:function(a){this.__ul.removeChild(a.__li);this.__controllers.slice(this.__controllers.indexOf(a),1);var b=this;h.defer(function(){b.onResize()})},destroy:function(){this.autoPlace&&x.removeChild(this.domElement)},addFolder:function(a){if(void 0!==this.__folders[a])throw Error('You already have a folder in this GUI by the name "'+a+'"');var b={name:a,parent:this};b.autoPlace=this.autoPlace;this.load&&this.load.folders&&this.load.folders[a]&&
      54 |     (b.closed=this.load.folders[a].closed,b.load=this.load.folders[a]);b=new m(b);this.__folders[a]=b;a=u(this,b.domElement);g.addClass(a,"folder");return b},open:function(){this.closed=!1},close:function(){this.closed=!0},onResize:function(){var a=this.getRoot();if(a.scrollable){var b=g.getOffset(a.__ul).top,d=0;h.each(a.__ul.childNodes,function(b){a.autoPlace&&b===a.__save_row||(d+=g.getHeight(b))});window.innerHeight-b-20<d?(g.addClass(a.domElement,m.CLASS_TOO_TALL),a.__ul.style.height=window.innerHeight-
>>>   55 |         b-20+"px"):(g.removeClass(a.domElement,m.CLASS_TOO_TALL),a.__ul.style.height="auto")}a.__resize_handle&&h.defer(function(){a.__resize_handle.style.height=a.__ul.offsetHeight+"px"});a.__closeButton&&(a.__closeButton.style.width=a.width+"px")},remember:function(){h.isUndefined(A)&&(A=new y,A.domElement.innerHTML=a);if(this.parent)throw Error("You can only call remember on a top level GUI.");var b=this;h.each(Array.prototype.slice.call(arguments),function(a){0==b.__rememberedObjects.length&&K(b);-1==
      56 |         b.__rememberedObjects.indexOf(a)&&b.__rememberedObjects.push(a)});this.autoPlace&&F(this,this.width)},getRoot:function(){for(var a=this;a.parent;)a=a.parent;return a},getSaveObject:function(){var a=this.load;a.closed=this.closed;0<this.__rememberedObjects.length&&(a.preset=this.preset,a.remembered||(a.remembered={}),a.remembered[this.preset]=B(this));a.folders={};h.each(this.__folders,function(b,d){a.folders[d]=b.getSaveObject()});return a},save:function(){this.load.remembered||(this.load.remembered=
      57 |     {});this.load.remembered[this.preset]=B(this);D(this,!1)},saveAs:function(a){this.load.remembered||(this.load.remembered={},this.load.remembered[z]=B(this,!0));this.load.remembered[a]=B(this);this.preset=a;E(this,a,!0)},revert:function(a){h.each(this.__controllers,function(b){this.getRoot().load.remembered?v(a||this.getRoot(),b):b.setValue(b.initialValue)},this);h.each(this.__folders,function(a){a.revert(a)});a||D(this.getRoot(),!1)},listen:function(a){var b=0==this.__listening.length;this.__listening.push(a);
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/assets/private/stats.min.js:3`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
       1 | // stats.js - http://github.com/mrdoob/stats.js
       2 | var Stats=function(){var l=Date.now(),m=l,g=0,n=Infinity,o=0,h=0,p=Infinity,q=0,r=0,s=0,f=document.createElement("div");f.id="stats";f.addEventListener("mousedown",function(b){b.preventDefault();t(++s%2)},!1);f.style.cssText="width:80px;opacity:0.9;cursor:pointer";var a=document.createElement("div");a.id="fps";a.style.cssText="padding:0 0 3px 3px;text-align:left;background-color:#002";f.appendChild(a);var i=document.createElement("div");i.id="fpsText";i.style.cssText="color:#0ff;font-family:Helvetica,Arial,sans-serif;font-size:9px;font-weight:bold;line-height:15px";
>>>    3 |     i.innerHTML="FPS";a.appendChild(i);var c=document.createElement("div");c.id="fpsGraph";c.style.cssText="position:relative;width:74px;height:30px;background-color:#0ff";for(a.appendChild(c);74>c.children.length;){var j=document.createElement("span");j.style.cssText="width:1px;height:30px;float:left;background-color:#113";c.appendChild(j)}var d=document.createElement("div");d.id="ms";d.style.cssText="padding:0 0 3px 3px;text-align:left;background-color:#020;display:none";f.appendChild(d);var k=document.createElement("div");
       4 |     k.id="msText";k.style.cssText="color:#0f0;font-family:Helvetica,Arial,sans-serif;font-size:9px;font-weight:bold;line-height:15px";k.innerHTML="MS";d.appendChild(k);var e=document.createElement("div");e.id="msGraph";e.style.cssText="position:relative;width:74px;height:30px;background-color:#0f0";for(d.appendChild(e);74>e.children.length;)j=document.createElement("span"),j.style.cssText="width:1px;height:30px;float:left;background-color:#131",e.appendChild(j);var t=function(b){s=b;switch(s){case 0:a.style.display=
       5 |         "block";d.style.display="none";break;case 1:a.style.display="none",d.style.display="block"}};return{REVISION:11,domElement:f,setMode:t,begin:function(){l=Date.now()},end:function(){var b=Date.now();g=b-l;n=Math.min(n,g);o=Math.max(o,g);k.textContent=g+" MS ("+n+"-"+o+")";var a=Math.min(30,30-30*(g/200));e.appendChild(e.firstChild).style.height=a+"px";r++;b>m+1E3&&(h=Math.round(1E3*r/(b-m)),p=Math.min(p,h),q=Math.max(q,h),i.textContent=h+" FPS ("+p+"-"+q+")",a=Math.min(30,30-30*(h/100)),c.appendChild(c.firstChild).style.height=
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `frontend/src/app/data-export/data-export.component.ts:72`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      70 |         this.confirmation = data.confirmation
      71 |         this.userData = data.userData
>>>   72 |         window.open('', '_blank', 'width=500')?.document.write(this.userData)
      73 |         this.lastSuccessfulTry = new Date()
      74 |         localStorage.setItem('lstdtxprt', JSON.stringify(this.lastSuccessfulTry))
```
</details>

---

## Logic (120)

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/challenges/forgedFeedback.ts:60`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
      58 |       async resolved () {
      59 |         const userId = (document.getElementById('userId') as HTMLInputElement).value
>>>   60 |         while (true) {
      61 |           if ((document.getElementById('userId') as HTMLInputElement).value !== userId) {
      62 |             break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/challenges/viewBasket.ts:60`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
      58 |       async resolved () {
      59 |         const bid = sessionStorage.getItem('bid')
>>>   60 |         while (true) {
      61 |           if (sessionStorage.getItem('bid') !== bid) {
      62 |             break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/challenges/viewBasket.ts:82`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
      80 |       async resolved () {
      81 |         const total = sessionStorage.getItem('itemTotal')
>>>   82 |         while (true) {
      83 |           if (sessionStorage.getItem('itemTotal') !== total) {
      84 |             break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:54`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
      52 |     }
      53 | 
>>>   54 |     while (true) {
      55 |       if (options.ignoreCase && inputElement.value.toLowerCase() === value.toLowerCase()) {
      56 |         break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:71`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
      69 |     )
      70 | 
>>>   71 |     while (true) {
      72 |       if (options.ignoreCase && inputElement.value.toLowerCase() !== value.toLowerCase()) {
      73 |         break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:88`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
      86 |     )
      87 | 
>>>   88 |     while (true) {
      89 |       if (inputElement.value !== '') {
      90 |         if (options.ignoreCase && inputElement.value.toLowerCase() !== value.toLowerCase()) {
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:107`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
     105 |     )
     106 | 
>>>  107 |     while (true) {
     108 |       if (inputElement.value && inputElement.value !== '') {
     109 |         break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:133`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
     131 | export function waitForElementsInnerHtmlToBe (elementSelector: string, value: string) {
     132 |   return async () => {
>>>  133 |     while (true) {
     134 |       const element = document.querySelector(
     135 |         elementSelector
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:161`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
     159 | export function waitForAngularRouteToBeVisited (route: string) {
     160 |   return async () => {
>>>  161 |     while (true) {
     162 |       if (window.location.hash.startsWith(`#/${route}`)) {
     163 |         break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:172`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
     170 | export function waitForLogIn () {
     171 |   return async () => {
>>>  172 |     while (true) {
     173 |       if (localStorage.getItem('token') !== null) {
     174 |         break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:183`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
     181 | export function waitForAdminLogIn () {
     182 |   return async () => {
>>>  183 |     while (true) {
     184 |       let role = ''
     185 |       try {
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:203`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
     201 | export function waitForLogOut () {
     202 |   return async () => {
>>>  203 |     while (true) {
     204 |       if (localStorage.getItem('token') === null) {
     205 |         break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:220`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
     218 |   const initialInnerWidth = window.innerWidth
     219 |   return async () => {
>>>  220 |     while (true) {
     221 |       if (window.innerHeight !== initialInnerHeight || window.innerWidth !== initialInnerWidth) {
     222 |         break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:235`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
     233 |     )
     234 | 
>>>  235 |     while (true) {
     236 |       if (selectElement.options[selectElement.selectedIndex].value === value) {
     237 |         break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:250`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
     248 |     )
     249 | 
>>>  250 |     while (true) {
     251 |       if (selectElement.options[selectElement.selectedIndex].value !== value) {
     252 |         break
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `frontend/src/hacking-instructor/helpers/helpers.ts:261`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
     259 | export function waitForRightUriQueryParamPair (key: string, value: string) {
     260 |   return async () => {
>>>  261 |     while (true) {
     262 |       const encodedValue: string = encodeURIComponent(value).replace(/%3A/g, ':')
     263 |       const encodedKey: string = encodeURIComponent(key).replace(/%3A/g, ':')
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `server.ts:428`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     426 |   /* User registration challenge verifications before finale takes over */
     427 |   app.post('/api/Users', (req: Request, res: Response, next: NextFunction) => {
>>>  428 |     if (req.body.email !== undefined && req.body.password !== undefined && req.body.passwordRepeat !== undefined) {
     429 |       if (req.body.email.length !== 0 && req.body.password.length !== 0) {
     430 |         req.body.email = req.body.email.trim()
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `server.ts:789`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     787 |     server.close()
     788 |   }
>>>  789 |   if (exitCode !== undefined) {
     790 |     process.exit(exitCode)
     791 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/2fa.ts:27`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      25 | 
      26 |     const user = await UserModel.findByPk(userId)
>>>   27 |     if (user == null) {
      28 |       throw new Error('No such user found!')
      29 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/2fa.ts:125`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     123 |     // Update db model and cached object
     124 |     const userModel = await UserModel.findByPk(user.id)
>>>  125 |     if (userModel == null) {
     126 |       throw new Error('No such user found!')
     127 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/2fa.ts:158`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     156 |     // Update db model and cached object
     157 |     const userModel = await UserModel.findByPk(user.id)
>>>  158 |     if (userModel == null) {
     159 |       throw new Error('No such user found!')
     160 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/basketItems.ts:72`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      70 |       challengeUtils.solveIf(challenges.basketManipulateChallenge, () => { return user && req.body.BasketId && user.bid != req.body.BasketId }) // eslint-disable-line eqeqeq
      71 |       if (req.body.quantity) {
>>>   72 |         if (item == null) {
      73 |           throw new Error('No such item found!')
      74 |         }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/basketItems.ts:87`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      85 | async function quantityCheck (req: Request, res: Response, next: NextFunction, id: number, quantity: number) {
      86 |   const product = await QuantityModel.findOne({ where: { ProductId: id } })
>>>   87 |   if (product == null) {
      88 |     throw new Error('No such product found!')
      89 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/changePassword.ts:28`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      26 | 
      27 |     const token = headers.authorization ? headers.authorization.substr('Bearer='.length) : null
>>>   28 |     if (token === null) {
      29 |       next(new Error('Blocked illegal activity by ' + connection.remoteAddress))
      30 |       return
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/currentUser.ts:30`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      28 |           // When fields are specified, return only those fields
      29 |           for (const field of requestedFields) {
>>>   30 |             if (user?.data[field as keyof typeof user.data] !== undefined) {
      31 |               baseUser[field] = user?.data[field as keyof typeof user.data]
      32 |             }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/currentUser.ts:54`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      52 |     challengeUtils.solveIf(challenges.passwordHashLeakChallenge, () => response?.user?.password)
      53 | 
>>>   54 |     if (req.query.callback === undefined) {
      55 |       res.json(response)
      56 |     } else {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/dataErasure.ts:40`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      38 |         }]
      39 |       })
>>>   40 |       if (answer == null) {
      41 |         throw new Error('No answer found!')
      42 |       }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/dataErasure.ts:44`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      42 |       }
      43 |       const question = await SecurityQuestionModel.findByPk(answer.SecurityQuestionId)
>>>   44 |       if (question == null) {
      45 |         throw new Error('No question found!')
      46 |       }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/deluxe.ts:20`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      18 |     try {
      19 |       const user = await UserModel.findOne({ where: { id: req.body.UserId, role: security.roles.customer } })
>>>   20 |       if (user == null) {
      21 |         res.status(400).json({ status: 'error', error: 'Something went wrong. Please try again!' })
      22 |         return
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/deluxe.ts:36`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      34 |       if (req.body.paymentMode === 'card') {
      35 |         const card = await CardModel.findOne({ where: { id: req.body.paymentId, UserId: req.body.UserId } })
>>>   36 |         if ((card == null) || card.expYear < new Date().getFullYear() || (card.expYear === new Date().getFullYear() && card.expMonth - 1 < new Date().getMonth())) {
      37 |           res.status(400).json({ status: 'error', error: 'Invalid Card' })
      38 |           return
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/languages.ts:38`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      36 | 
      37 |         let backendPercentage = 0
>>>   38 |         if (backendEnContent !== null) {
      39 |           try {
      40 |             const backendContent = await readFile('i18n/' + fileName, 'utf-8')
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/languages.ts:48`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      46 |         }
      47 | 
>>>   48 |         const percentage = Math.round(backendEnContent !== null ? (frontendPercentage + backendPercentage) / 2 : frontendPercentage)
      49 |         const gauge = (percentage > 80 ? 'full' : (percentage > 60 ? 'three-quarters' : (percentage > 40 ? 'half' : (percentage > 20 ? 'quarter' : 'empty'))))
      50 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/languages.ts:67`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      65 |       const results = await Promise.all(languagePromises)
      66 |       results.forEach((lang) => {
>>>   67 |         if (lang !== null) {
      68 |           languages.push(lang)
      69 |         }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/profileImageFileUpload.ts:18`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      16 |     const file = req.file
      17 |     const buffer = file?.buffer
>>>   18 |     if (buffer === undefined) {
      19 |       res.status(500)
      20 |       next(new Error('Illegal file type'))
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/profileImageFileUpload.ts:24`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      22 |     }
      23 |     const uploadedFileType = await fileType.fromBuffer(buffer)
>>>   24 |     if (uploadedFileType === undefined) {
      25 |       res.status(500)
      26 |       next(new Error('Illegal file type'))
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/profileImageFileUpload.ts:29`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      27 |       return
      28 |     }
>>>   29 |     if (uploadedFileType === null || !uploadedFileType.mime.startsWith('image')) {
      30 |       res.status(415)
      31 |       next(new Error(`Profile image upload does not accept this file type${uploadedFileType ? (': ' + uploadedFileType.mime) : '.'}`))
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/profileImageUrlUpload.ts:18`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      16 | export function profileImageUrlUpload () {
      17 |   return async (req: Request, res: Response, next: NextFunction) => {
>>>   18 |     if (req.body.imageUrl !== undefined) {
      19 |       const url = req.body.imageUrl
      20 |       if (url.match(/(.)*solve\/challenges\/server-side(.)*/) !== null) req.app.locals.abused_ssrf_bug = true
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/saveLoginIp.ts:17`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      15 |   return async (req: Request, res: Response, next: NextFunction) => {
      16 |     const loggedInUser = security.authenticatedUsers.from(req)
>>>   17 |     if (loggedInUser !== undefined) {
      18 |       let lastLoginIp = req.headers['true-client-ip']
      19 |       if (Array.isArray(lastLoginIp)) {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/saveLoginIp.ts:27`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      25 |         lastLoginIp = security.sanitizeSecure(lastLoginIp ?? '')
      26 |       }
>>>   27 |       if (lastLoginIp === undefined) {
      28 |         lastLoginIp = utils.toSimpleIpAddress(req.socket.remoteAddress ?? '')
      29 |       }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/showProductReviews.ts:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      39 |       const user = security.authenticatedUsers.from(req)
      40 |       for (let i = 0; i < reviews.length; i++) {
>>>   41 |         if (user === undefined || reviews[i].likedBy.includes(user.data.email)) {
      42 |           reviews[i].liked = true
      43 |         }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/trackOrder.ts:21`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      19 |       const result = utils.queryResultToJson(order)
      20 |       challengeUtils.solveIf(challenges.noSqlOrdersChallenge, () => { return result.data.length > 1 })
>>>   21 |       if (result.data[0] === undefined) {
      22 |         result.data[0] = { orderId: id }
      23 |       }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/userProfile.ts:58`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      56 | 
      57 |     if (utils.isChallengeEnabled(challenges.usernameXssChallenge)) {
>>>   58 |       if (username?.match(/#{(.*)}/) !== null) {
      59 |         req.app.locals.abused_ssti_bug = true
      60 |         const code = username?.substring(2, username.length - 1)
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/userProfile.ts:94`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      92 | 
      93 |       challengeUtils.solveIf(challenges.usernameXssChallenge, () => {
>>>   94 |         return username && user?.profileImage.match(/;[ ]*script-src(.)*'unsafe-inline'/g) !== null && username.includes('<script>alert(`xss`)</script>')
      95 |       })
      96 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/verify.ts:101`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      99 | export const serverSideChallenges = () => (req: Request, res: Response, next: NextFunction) => {
     100 |   if (req.query.key === 'tRy_H4rd3r_n0thIng_iS_Imp0ssibl3') {
>>>  101 |     if (challengeUtils.notSolved(challenges.sstiChallenge) && req.app.locals.abused_ssti_bug === true) {
     102 |       challengeUtils.solve(challenges.sstiChallenge)
     103 |       res.status(204).send()
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/verify.ts:107`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     105 |     }
     106 | 
>>>  107 |     if (challengeUtils.notSolved(challenges.ssrfChallenge) && req.app.locals.abused_ssrf_bug === true) {
     108 |       challengeUtils.solve(challenges.ssrfChallenge)
     109 |       res.status(204).send()
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/verify.ts:121`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     119 |     const decoded = jws.decode(token) ? jwt.decode(token) : null
     120 | 
>>>  121 |     if (decoded === null || typeof decoded === 'string') {
     122 |       return
     123 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/verify.ts:126`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     124 | 
     125 |     jwt.verify(token, security.publicKey, (err: jwt.VerifyErrors | null) => {
>>>  126 |       if (err === null) {
     127 |         challengeUtils.solveIf(challenge, () => {
     128 |           return hasAlgorithm(token, algorithm) && hasEmail(decoded as { data: { email: string } }, email)
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/verify.ts:220`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     218 |   void osaft.reload().then(() => {
     219 |     for (const product of config.get<ProductConfig[]>('products')) {
>>>  220 |       if (product.urlForProductTamperingChallenge !== undefined) {
     221 |         urlForProductTamperingChallenge = product.urlForProductTamperingChallenge
     222 |         break
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/videoHandler.ts:87`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      85 | 
      86 | function videoPath () {
>>>   87 |   if (config.get<string>('application.promotion.video') !== null) {
      88 |     const video = utils.extractFilename(config.get<string>('application.promotion.video'))
      89 |     return 'frontend/dist/frontend/assets/public/videos/' + video
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/vulnCodeSnippet.ts:45`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      43 |   try {
      44 |     const snippetData = await retrieveCodeSnippet(req.params.challenge)
>>>   45 |     if (snippetData == null) {
      46 |       res.status(404).json({ status: 'error', error: `No code challenge for challenge key: ${req.params.challenge}` })
      47 |       return
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/vulnCodeSnippet.ts:62`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      60 | 
      61 | export const getVerdict = (vulnLines: number[], neutralLines: number[], selectedLines: number[]) => {
>>>   62 |   if (selectedLines === undefined) return false
      63 |   if (vulnLines.length > selectedLines.length) return false
      64 |   if (!vulnLines.every(e => selectedLines.includes(e))) return false
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `routes/vulnCodeSnippet.ts:75`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      73 |   try {
      74 |     snippetData = await retrieveCodeSnippet(key)
>>>   75 |     if (snippetData == null) {
      76 |       res.status(404).json({ status: 'error', error: `No code challenge for challenge key: ${key}` })
      77 |       return
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `rsn/rsnUtil.ts:65`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      63 |     try {
      64 |       const snippet = await retrieveCodeSnippet(val.split('_')[0])
>>>   65 |       if (snippet == null) continue
      66 |       const fileData = fs.readFileSync(fixesPath + '/' + val).toString()
      67 |       const diff = diffLines(filterString(fileData), filterString(snippet.snippet))
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/hacking-instructor/index.ts:177`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     175 | 
     176 | export function hasInstructions (challengeName: string): boolean {
>>>  177 |   return challengeInstructions.find(({ name }) => name === challengeName) !== undefined
     178 | }
     179 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/EffectComposer.js:9`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
       7 | 	this.renderer = renderer;
       8 | 
>>>    9 | 	if ( renderTarget === undefined ) {
      10 | 
      11 | 		var width = window.innerWidth || 1;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/EffectComposer.js:27`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      25 | 	this.passes = [];
      26 | 
>>>   27 | 	if ( THREE.CopyShader === undefined )
      28 | 		console.error( "THREE.EffectComposer relies on THREE.CopyShader" );
      29 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/EffectComposer.js:107`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     105 | 	reset: function ( renderTarget ) {
     106 | 
>>>  107 | 		if ( renderTarget === undefined ) {
     108 | 
     109 | 			renderTarget = this.renderTarget1.clone();
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:27`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      25 | 
      26 |     this.object = object;
>>>   27 |     this.domElement = ( domElement !== undefined ) ? domElement : document;
      28 | 
      29 |     // API
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:106`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     104 |     this.rotateLeft = function ( angle ) {
     105 | 
>>>  106 |         if ( angle === undefined ) {
     107 | 
     108 |             angle = getAutoRotationAngle();
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:118`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     116 |     this.rotateUp = function ( angle ) {
     117 | 
>>>  118 |         if ( angle === undefined ) {
     119 | 
     120 |             angle = getAutoRotationAngle();
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:159`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     157 |         var element = scope.domElement === document ? scope.domElement.body : scope.domElement;
     158 | 
>>>  159 |         if ( scope.object.fov !== undefined ) {
     160 | 
     161 |             // perspective
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:172`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     170 |             scope.panUp( 2 * delta.y * targetDistance / element.clientHeight );
     171 | 
>>>  172 |         } else if ( scope.object.top !== undefined ) {
     173 | 
     174 |             // orthographic
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:189`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     187 |     this.dollyIn = function ( dollyScale ) {
     188 | 
>>>  189 |         if ( dollyScale === undefined ) {
     190 | 
     191 |             dollyScale = getZoomScale();
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:201`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     199 |     this.dollyOut = function ( dollyScale ) {
     200 | 
>>>  201 |         if ( dollyScale === undefined ) {
     202 | 
     203 |             dollyScale = getZoomScale();
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:285`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     283 |     function onMouseDown( event ) {
     284 | 
>>>  285 |         if ( scope.enabled === false ) { return; }
     286 |         event.preventDefault();
     287 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:289`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     287 | 
     288 |         if ( event.button === 0 ) {
>>>  289 |             if ( scope.noRotate === true ) { return; }
     290 | 
     291 |             state = STATE.ROTATE;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:296`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     294 | 
     295 |         } else if ( event.button === 1 ) {
>>>  296 |             if ( scope.noZoom === true ) { return; }
     297 | 
     298 |             state = STATE.DOLLY;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:303`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     301 | 
     302 |         } else if ( event.button === 2 ) {
>>>  303 |             if ( scope.noPan === true ) { return; }
     304 | 
     305 |             state = STATE.PAN;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:319`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     317 |     function onMouseMove( event ) {
     318 | 
>>>  319 |         if ( scope.enabled === false ) return;
     320 | 
     321 |         event.preventDefault();
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:327`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     325 |         if ( state === STATE.ROTATE ) {
     326 | 
>>>  327 |             if ( scope.noRotate === true ) return;
     328 | 
     329 |             rotateEnd.set( event.clientX, event.clientY );
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:341`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     339 |         } else if ( state === STATE.DOLLY ) {
     340 | 
>>>  341 |             if ( scope.noZoom === true ) return;
     342 | 
     343 |             dollyEnd.set( event.clientX, event.clientY );
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:360`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     358 |         } else if ( state === STATE.PAN ) {
     359 | 
>>>  360 |             if ( scope.noPan === true ) return;
     361 | 
     362 |             panEnd.set( event.clientX, event.clientY );
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:378`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     376 |     function onMouseUp( /* event */ ) {
     377 | 
>>>  378 |         if ( scope.enabled === false ) return;
     379 | 
     380 |         // Greggman fix: https://github.com/greggman/three.js/commit/fde9f9917d6d8381f06bf22cdff766029d1761be
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:390`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     388 |     function onMouseWheel( event ) {
     389 | 
>>>  390 |         if ( scope.enabled === false || scope.noZoom === true ) return;
     391 | 
     392 |         var delta = 0;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:418`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     416 |     function onKeyDown( event ) {
     417 | 
>>>  418 |         if ( scope.enabled === false ) { return; }
     419 |         if ( scope.noKeys === true ) { return; }
     420 |         if ( scope.noPan === true ) { return; }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:457`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     455 |     function touchstart( event ) {
     456 | 
>>>  457 |         if ( scope.enabled === false ) { return; }
     458 | 
     459 |         switch ( event.touches.length ) {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:462`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     460 | 
     461 |             case 1:	// one-fingered touch: rotate
>>>  462 |                 if ( scope.noRotate === true ) { return; }
     463 | 
     464 |                 state = STATE.TOUCH_ROTATE;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:470`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     468 | 
     469 |             case 2:	// two-fingered touch: dolly
>>>  470 |                 if ( scope.noZoom === true ) { return; }
     471 | 
     472 |                 state = STATE.TOUCH_DOLLY;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:481`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     479 | 
     480 |             case 3: // three-fingered touch: pan
>>>  481 |                 if ( scope.noPan === true ) { return; }
     482 | 
     483 |                 state = STATE.TOUCH_PAN;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:496`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     494 |     function touchmove( event ) {
     495 | 
>>>  496 |         if ( scope.enabled === false ) { return; }
     497 | 
     498 |         event.preventDefault();
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:506`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     504 | 
     505 |             case 1: // one-fingered touch: rotate
>>>  506 |                 if ( scope.noRotate === true ) { return; }
     507 |                 if ( state !== STATE.TOUCH_ROTATE ) { return; }
     508 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:521`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     519 | 
     520 |             case 2: // two-fingered touch: dolly
>>>  521 |                 if ( scope.noZoom === true ) { return; }
     522 |                 if ( state !== STATE.TOUCH_DOLLY ) { return; }
     523 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:545`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     543 | 
     544 |             case 3: // three-fingered touch: pan
>>>  545 |                 if ( scope.noPan === true ) { return; }
     546 |                 if ( state !== STATE.TOUCH_PAN ) { return; }
     547 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/OrbitControls.js:565`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     563 |     function touchend( /* event */ ) {
     564 | 
>>>  565 |         if ( scope.enabled === false ) { return; }
     566 | 
     567 |         state = STATE.NONE;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/RenderPass.js:13`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      11 | 
      12 | 	this.clearColor = clearColor;
>>>   13 | 	this.clearAlpha = ( clearAlpha !== undefined ) ? clearAlpha : 1;
      14 | 
      15 | 	this.oldClearColor = new THREE.Color();
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/assets/private/ShaderPass.js:7`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
       5 | THREE.ShaderPass = function ( shader, textureID ) {
       6 | 
>>>    7 | 	this.textureID = ( textureID !== undefined ) ? textureID : "tDiffuse";
       8 | 
       9 | 	this.uniforms = THREE.UniformsUtils.clone( shader.uniforms );
```
</details>

---

### [~] Side-Effect in Condition

- **File:** `frontend/src/assets/private/stats.min.js:5`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Pre/post increment used in a standalone statement may indicate logic confusion.

**Fix:** Ensure increment is intentional and not a mistyped comparison (== vs =).

<details>
<summary>Code</summary>

```
       3 |     i.innerHTML="FPS";a.appendChild(i);var c=document.createElement("div");c.id="fpsGraph";c.style.cssText="position:relative;width:74px;height:30px;background-color:#0ff";for(a.appendChild(c);74>c.children.length;){var j=document.createElement("span");j.style.cssText="width:1px;height:30px;float:left;background-color:#113";c.appendChild(j)}var d=document.createElement("div");d.id="ms";d.style.cssText="padding:0 0 3px 3px;text-align:left;background-color:#020;display:none";f.appendChild(d);var k=document.createElement("div");
       4 |     k.id="msText";k.style.cssText="color:#0f0;font-family:Helvetica,Arial,sans-serif;font-size:9px;font-weight:bold;line-height:15px";k.innerHTML="MS";d.appendChild(k);var e=document.createElement("div");e.id="msGraph";e.style.cssText="position:relative;width:74px;height:30px;background-color:#0f0";for(d.appendChild(e);74>e.children.length;)j=document.createElement("span"),j.style.cssText="width:1px;height:30px;float:left;background-color:#131",e.appendChild(j);var t=function(b){s=b;switch(s){case 0:a.style.display=
>>>    5 |         "block";d.style.display="none";break;case 1:a.style.display="none",d.style.display="block"}};return{REVISION:11,domElement:f,setMode:t,begin:function(){l=Date.now()},end:function(){var b=Date.now();g=b-l;n=Math.min(n,g);o=Math.max(o,g);k.textContent=g+" MS ("+n+"-"+o+")";var a=Math.min(30,30-30*(g/200));e.appendChild(e.firstChild).style.height=a+"px";r++;b>m+1E3&&(h=Math.round(1E3*r/(b-m)),p=Math.min(p,h),q=Math.max(q,h),i.textContent=h+" FPS ("+p+"-"+q+")",a=Math.min(30,30-30*(h/100)),c.appendChild(c.firstChild).style.height=
       6 |         a+"px",m=b,r=0);return b},update:function(){l=this.end()}}};
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/Services/basket.service.ts:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      82 |   getGuestBasketItems (): GuestBasketItem[] {
      83 |     const rawGuestBasket = sessionStorage.getItem(this.guestBasketKey)
>>>   84 |     if (rawGuestBasket == null) {
      85 |       return []
      86 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/Services/basket.service.ts:128`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     126 |     const guestBasketItems = this.getGuestBasketItems()
     127 |     const guestItemToUpdate = guestBasketItems.find(item => item.ProductId === productId)
>>>  128 |     if (guestItemToUpdate == null) {
     129 |       return
     130 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/basket/basket.component.ts:32`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      30 | 
      31 |   checkout (): void {
>>>   32 |     if (localStorage.getItem('token') == null) {
      33 |       this.ngZone.run(async () => await this.router.navigate(['/login'], {
      34 |         queryParams: {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/coding-challenge-page/coding-challenge-page.component.ts:77`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      75 |   onFindItSolved (): void {
      76 |     this.findItSolved = true
>>>   77 |     if (this.fixes !== null) {
      78 |       setTimeout(() => {
      79 |         this.fixItSection()?.nativeElement?.scrollIntoView({ behavior: 'smooth' })
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/product/product.component.ts:40`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      38 | 
      39 |   addToBasket(id?: number) {
>>>   40 |     if (id == null) {
      41 |       return
      42 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/purchase-basket/purchase-basket.component.ts:55`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      53 |     this.load()
      54 | 
>>>   55 |     if (localStorage.getItem('token') == null) {
      56 |       this.userEmail = '(anonymous)'
      57 |       return
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/purchase-basket/purchase-basket.component.ts:73`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      71 | 
      72 |   load () {
>>>   73 |     if (localStorage.getItem('token') == null) {
      74 |       this.loadGuestBasket()
      75 |       return
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/purchase-basket/purchase-basket.component.ts:138`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     136 | 
     137 |   delete (id) {
>>>  138 |     if (localStorage.getItem('token') == null) {
     139 |       this.basketService.removeGuestBasketItem(id)
     140 |       this.load()
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/purchase-basket/purchase-basket.component.ts:162`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     160 | 
     161 |   addToQuantity (id, value) {
>>>  162 |     if (localStorage.getItem('token') == null) {
     163 |       const existingGuestItem = this.basketService.getGuestBasketItems().find(item => item.ProductId === id)
     164 |       if (existingGuestItem == null) {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/search-result/search-result.component.ts:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      82 |             return dataTableEntry.id === quantity.ProductId
      83 |           })
>>>   84 |           if (entry === undefined) {
      85 |             continue
      86 |           }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/search-result/search-result.component.ts:206`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     204 | 
     205 |   isLoggedIn (): boolean {
>>>  206 |     return localStorage.getItem('token') !== null
     207 |   }
     208 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/track-result/track-result.component.ts:53`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      51 |       this.results.totalPrice = results.data[0].totalPrice
      52 |       this.results.products = results.data[0].products
>>>   53 |       this.results.eta = results.data[0].eta !== undefined ? results.data[0].eta : '?'
      54 |       this.results.bonus = results.data[0].bonus
      55 |       this.dataSource.data = this.results.products
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/filter-settings/query-params-converters.ts:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      23 |     filterSetting.categories = queryParams.categories.split(',')
      24 |   }
>>>   25 |   if (queryParams.showDisabledChallenges !== undefined) {
      26 |     filterSetting.showDisabledChallenges = queryParams.showDisabledChallenges === 'true'
      27 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/helpers/challenge-filtering.ts:42`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      40 |       // filter by status
      41 |       .filter((challenge) => {
>>>   42 |         if (filterSetting.status === null) {
      43 |           return true
      44 |         }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/helpers/challenge-filtering.ts:49`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      47 |       // filter disabled challenges
      48 |       .filter((challenge) => {
>>>   49 |         if (challenge.disabledEnv === null) {
      50 |           return true
      51 |         }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/helpers/challenge-filtering.ts:56`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      54 |       // filter by search query
      55 |       .filter((challenge) => {
>>>   56 |         if (filterSetting.searchQuery === null) {
      57 |           return true
      58 |         }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/helpers/challenge-filtering.ts:75`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      73 | 
      74 |         const tutorialChallenges = challenges.filter(
>>>   75 |           (challenge) => challenge.tutorialOrder !== null
      76 |         )
      77 |         const allTutorialChallengesSolved = tutorialChallenges.every((challenge) => challenge.solved)
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/helpers/challenge-filtering.ts:81`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      79 |         if (allTutorialChallengesSolved) {
      80 |           return true
>>>   81 |         } else if (!allTutorialChallengesSolved && challenge.tutorialOrder === null) {
      82 |           // there are still unsolved tutorial challenges, but this challenge is not a tutorial challenge so we don't want to show it
      83 |           return false
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/components/challenge-card/challenge-card.component.ts:50`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      48 |       if (
      49 |         lastUnlockedKey === challenge?.key &&
>>>   50 |         this.previousHintsUnlocked !== undefined &&
      51 |         currentHintsUnlocked !== this.previousHintsUnlocked
      52 |       ) {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/components/challenges-unavailable-warning/challenges-unavailable-warning.component.ts:22`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      20 | 
      21 |   private readonly disabledChallenges = computed(() =>
>>>   22 |     this.challenges().filter(challenge => challenge.disabledEnv !== null)
      23 |   )
      24 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/components/filter-settings/filter-settings.component.ts:93`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      91 |   public canBeReset (): boolean {
      92 |     return this.filterSetting.difficulties.length > 0 ||
>>>   93 |       this.filterSetting.status !== null ||
      94 |       this.filterSetting.tags.length > 0 ||
      95 |       this.filterSetting.categories.length > 0 ||
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/components/tutorial-mode-warning/tutorial-mode-warning.component.ts:24`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      22 |     }
      23 |     return !this.allChallenges()
>>>   24 |       .filter(challenge => challenge.tutorialOrder !== null)
      25 |       .every(challenge => challenge.solved)
      26 |   })
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/score-board/components/filter-settings/pipes/difficulty-selection-summary.pipe.ts:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      29 |   let currentGroup: DifficultyGroup = null
      30 |   for (const difficulty of difficulties) {
>>>   31 |     if (currentGroup === null) {
      32 |       currentGroup = { start: difficulty, end: difficulty }
      33 |     } else {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/coding-challenge-page/components/coding-challenge-find-it/coding-challenge-find-it.component.spec.ts:33`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      31 | 
      32 |     function hasClass(className: string): boolean {
>>>   33 |         return editorDom().querySelector(`.${className}`) !== null
      34 |     }
      35 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `frontend/src/app/coding-challenge-page/components/coding-challenge-find-it/coding-challenge-find-it.component.ts:194`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     192 |         if (!target.closest('.cm-content')) return false
     193 |         const pos = view.posAtCoords({ x: event.clientX, y: event.clientY })
>>>  194 |         if (pos === null) return false
     195 |         const line = view.state.doc.lineAt(pos)
     196 |         event.preventDefault()
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `data/static/codefixes/exposedMetricsChallenge_1.ts:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      39 |     server.close()
      40 |   }
>>>   41 |   if (exitCode !== undefined) {
      42 |     process.exit(exitCode)
      43 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `data/static/codefixes/exposedMetricsChallenge_2.ts:37`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      35 |     server.close()
      36 |   }
>>>   37 |   if (exitCode !== undefined) {
      38 |     process.exit(exitCode)
      39 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `data/static/codefixes/exposedMetricsChallenge_3_correct.ts:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      39 |     server.close()
      40 |   }
>>>   41 |   if (exitCode !== undefined) {
      42 |     process.exit(exitCode)
      43 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `data/static/codefixes/noSqlReviewsChallenge_1.ts:5`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
       3 |     const user = security.authenticatedUsers.from(req)
       4 | 
>>>    5 |     if (req.body.id['$ne'] !== undefined) {
       6 |       res.status(400).send()
       7 |       return
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `data/static/codefixes/restfulXssChallenge_1_correct.ts:22`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      20 |             return dataTableEntry.id === quantity.ProductId
      21 |           })
>>>   22 |           if (entry === undefined) {
      23 |             continue
      24 |           }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `data/static/codefixes/restfulXssChallenge_2.ts:23`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      21 |             return dataTableEntry.id === quantity.ProductId
      22 |           })
>>>   23 |           if (entry === undefined) {
      24 |             continue
      25 |           }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `data/static/codefixes/restfulXssChallenge_3.ts:23`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      21 |             return dataTableEntry.id === quantity.ProductId
      22 |           })
>>>   23 |           if (entry === undefined) {
      24 |             continue
      25 |           }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `data/static/codefixes/restfulXssChallenge_4.ts:23`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      21 |             return dataTableEntry.id === quantity.ProductId
      22 |           })
>>>   23 |           if (entry === undefined) {
      24 |             continue
      25 |           }
```
</details>

---

## Performance (20)

### [!] SELECT * Query

- **File:** `routes/login.ts:34`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      32 |   return (req: Request, res: Response, next: NextFunction) => {
      33 |     verifyPreLoginChallenges(req) // vuln-code-snippet hide-line
>>>   34 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: UserModel, plain: true }) // vuln-code-snippet vuln-line loginAdminChallenge loginBenderChallenge loginJimChallenge
      35 |       .then((authenticatedUser) => { // vuln-code-snippet neutral-line loginAdminChallenge loginBenderChallenge loginJimChallenge
      36 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!] SELECT * Query

- **File:** `routes/search.ts:23`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      21 |     let criteria: any = req.query.q === 'undefined' ? '' : req.query.q ?? ''
      22 |     criteria = (criteria.length <= 200) ? criteria : criteria.substring(0, 200)
>>>   23 |     models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`) // vuln-code-snippet vuln-line unionSqlInjectionChallenge dbSchemaChallenge
      24 |       .then(([products]: any) => {
      25 |         const dataString = JSON.stringify(products)
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/dbSchemaChallenge_1.ts:5`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
       3 |     let criteria: any = req.query.q === 'undefined' ? '' : req.query.q ?? ''
       4 |     criteria = (criteria.length <= 200) ? criteria : criteria.substring(0, 200)
>>>    5 |     models.sequelize.query("SELECT * FROM Products WHERE ((name LIKE '%"+criteria+"%' OR description LIKE '%"+criteria+"%') AND deletedAt IS NULL) ORDER BY name")
       6 |       .then(([products]: any) => {
       7 |         const dataString = JSON.stringify(products)
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/dbSchemaChallenge_2_correct.ts:6`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
       4 |     criteria = (criteria.length <= 200) ? criteria : criteria.substring(0, 200)
       5 |     models.sequelize.query(
>>>    6 |         `SELECT * FROM Products WHERE ((name LIKE '%:criteria%' OR description LIKE '%:criteria%') AND deletedAt IS NULL) ORDER BY name`,
       7 |         { replacements: { criteria } }
       8 |       ).then(([products]: any) => {
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/dbSchemaChallenge_3.ts:11`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
       9 |       return
      10 |     }
>>>   11 |     models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)
      12 |       .then(([products]: any) => {
      13 |         const dataString = JSON.stringify(products)
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginAdminChallenge_1.ts:18`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      16 |       res.status(451).send(res.__('SQL Injection detected.'))
      17 |     }
>>>   18 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: true })
      19 |       .then((authenticatedUser) => {
      20 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginAdminChallenge_2.ts:15`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`,
      16 |       { bind: [ req.body.email ], model: models.User, plain: true })
      17 |       .then((authenticatedUser) => {
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginAdminChallenge_3.ts:15`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = $2 AND deletedAt IS NULL`,
      16 |       { bind: [ req.body.email, req.body.password ], model: models.User, plain: true })
      17 |       .then((authenticatedUser) => {
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginAdminChallenge_4_correct.ts:15`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = $2 AND deletedAt IS NULL`,
      16 |       { bind: [ req.body.email, security.hash(req.body.password) ], model: models.User, plain: true })
      17 |       .then((authenticatedUser) => {
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginBenderChallenge_1.ts:18`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      16 |       res.status(451).send(res.__('SQL Injection detected.'))
      17 |     }
>>>   18 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: true })
      19 |       .then((authenticatedUser) => {
      20 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginBenderChallenge_2_correct.ts:15`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = $mail AND password = $pass AND deletedAt IS NULL`,
      16 |       { bind: { mail: req.body.email, pass: security.hash(req.body.password) }, model: models.User, plain: true })
      17 |       .then((authenticatedUser) => {
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginBenderChallenge_3.ts:15`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = :mail AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`,
      16 |       { replacements: { mail: req.body.email }, model: models.User, plain: true })
      17 |       .then((authenticatedUser) => {
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginBenderChallenge_4.ts:15`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: false })
      16 |       .then((authenticatedUser) => {
      17 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginJimChallenge_1_correct.ts:15`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = $2 AND deletedAt IS NULL`,
      16 |       { bind: [ req.body.email, security.hash(req.body.password) ], model: models.User, plain: true })
      17 |       .then((authenticatedUser) => {
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginJimChallenge_2.ts:15`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: false })
      16 |       .then((authenticatedUser) => {
      17 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginJimChallenge_3.ts:15`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      13 | 
      14 |   return (req: Request, res: Response, next: NextFunction) => {
>>>   15 |     models.sequelize.query(`SELECT * FROM Users WHERE email = ? AND password = ? AND deletedAt IS NULL`,
      16 |       { replacements: [ req.body.email, req.body.password ], model: models.User, plain: true })
      17 |       .then((authenticatedUser) => {
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/loginJimChallenge_4.ts:18`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
      16 |       res.status(451).send(res.__('SQL Injection detected.'))
      17 |     }
>>>   18 |     models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: true })
      19 |       .then((authenticatedUser) => {
      20 |         const user = utils.queryResultToJson(authenticatedUser)
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/unionSqlInjectionChallenge_1.ts:6`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
       4 |     criteria = (criteria.length <= 200) ? criteria : criteria.substring(0, 200)
       5 |     criteria.replace(/"|'|;|and|or/i, "")
>>>    6 |     models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)
       7 |       .then(([products]: any) => {
       8 |         const dataString = JSON.stringify(products)
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/unionSqlInjectionChallenge_2_correct.ts:6`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
       4 |     criteria = (criteria.length <= 200) ? criteria : criteria.substring(0, 200)
       5 |     models.sequelize.query(
>>>    6 |         `SELECT * FROM Products WHERE ((name LIKE '%:criteria%' OR description LIKE '%:criteria%') AND deletedAt IS NULL) ORDER BY name`,
       7 |         { replacements: { criteria } }
       8 |       ).then(([products]: any) => {
```
</details>

---

### [!] SELECT * Query

- **File:** `data/static/codefixes/unionSqlInjectionChallenge_3.ts:10`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.

**Fix:** Select only the columns you need.

<details>
<summary>Code</summary>

```
       8 |       return
       9 |     }
>>>   10 |     models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)
      11 |       .then(([products]: any) => {
      12 |         const dataString = JSON.stringify(products)
```
</details>

---

## Code Quality (12)

### [~] UNCLEAR require Error Message

- **File:** `data/static/codefixes/web3WalletChallenge_1.sol:21`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      19 | 
      20 |   function withdraw(uint _amount) public {
>>>   21 |     require(_amount <= 0.1 ether, "Withdrawal amount must be less than or equal to 0.1 ether");
      22 |     require(balances[msg.sender] >= _amount, "Insufficient balance");
      23 |     if (userWithdrawing[msg.sender] <= 1) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/codefixes/web3WalletChallenge_1.sol:30`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      28 |     }
      29 |     (bool result, ) = msg.sender.call{ value: _amount }("");
>>>   30 |     require(result, "Withdrawal call failed");
      31 |     balances[msg.sender] = balances[msg.sender] - _amount;
      32 |     userWithdrawing[msg.sender] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/codefixes/web3WalletChallenge_2.sol:21`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      19 | 
      20 |   function withdraw(uint _amount) public {
>>>   21 |     require(_amount <= 0.1 ether, "Withdrawal amount must be less than or equal to 0.1 ether");
      22 |     require(balances[msg.sender] >= _amount, "Insufficient balance");
      23 |     if (userWithdrawing[msg.sender] <= 1) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/codefixes/web3WalletChallenge_2.sol:30`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      28 |     }
      29 |     (bool result, ) = msg.sender.call{ value: _amount }("");
>>>   30 |     require(result, "Withdrawal call failed");
      31 |     userWithdrawing[msg.sender] = 0;
      32 |     balances[msg.sender] -= _amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/codefixes/web3WalletChallenge_3_correct.sol:21`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      19 | 
      20 |   function withdraw(uint _amount) public {
>>>   21 |     require(_amount <= 0.1 ether, "Withdrawal amount must be less than or equal to 0.1 ether");
      22 |     require(balances[msg.sender] >= _amount, "Insufficient balance");
      23 |     if (userWithdrawing[msg.sender] <= 1) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/codefixes/web3WalletChallenge_3_correct.sol:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      29 |     balances[msg.sender] -= _amount;
      30 |     (bool result, ) = msg.sender.call{ value: _amount }("");
>>>   31 |     require(result, "Withdrawal call failed");
      32 |     userWithdrawing[msg.sender] = 0;
      33 |   }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/codefixes/web3WalletChallenge_4.sol:21`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      19 | 
      20 |   function withdraw(uint _amount) public {
>>>   21 |     require(_amount <= 0.1 ether, "Withdrawal amount must be less than or equal to 0.1 ether");
      22 |     require(balances[msg.sender] <= _amount, "Insufficient balance");
      23 |     if (userWithdrawing[msg.sender] >= 1) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/codefixes/web3WalletChallenge_4.sol:30`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      28 |     }
      29 |     (bool result, ) = msg.sender.call{ value: _amount }("");
>>>   30 |     require(result, "Withdrawal call failed");
      31 |     balances[msg.sender] += _amount;
      32 |     userWithdrawing[msg.sender] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/web3-snippets/BEEToken.sol:30`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      28 | 
      29 |     modifier onlyOwner() {
>>>   30 |         require(msg.sender == _owner, "Only the contract owner can call this function");
      31 |         _;
      32 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/web3-snippets/BeeFaucet.sol:16`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      14 |     function withdraw(uint8 amount) public {
      15 |         balance -= amount;
>>>   16 |         require(balance >= 0, "Withdrew more than the account balance!");
      17 |         token.transfer(msg.sender, uint256(amount) * 1000000000000000000);
      18 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/web3-snippets/ETHWalletBank.sol:23`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      21 | 
      22 |   function withdraw(uint _amount) public {
>>>   23 |     require(_amount <= 0.1 ether, "Withdrawal amount must be less than or equal to 0.1 ether");
      24 |     require(balances[msg.sender] >= _amount, "Insufficient balance");
      25 |     if (userWithdrawing[msg.sender] <= 1) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `data/static/web3-snippets/ETHWalletBank.sol:33`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      31 |     }
      32 |     (bool result, ) = msg.sender.call{ value: _amount }(""); // vuln-code-snippet neutral-line web3WalletChallenge
>>>   33 |     require(result, "Withdrawal call failed"); // vuln-code-snippet neutral-line web3WalletChallenge
      34 |     balances[msg.sender] -= _amount; // vuln-code-snippet vuln-line web3WalletChallenge
      35 |     if(userWithdrawing[msg.sender] == 2) // vuln-code-snippet hide-line
```
</details>

---

## Xss (9)

### [!] innerHTML assignment
- **File:** `frontend/src/assets/private/dat.gui.min.js:1`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `frontend/src/assets/private/dat.gui.min.js:13`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `frontend/src/assets/private/dat.gui.min.js:23`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `frontend/src/assets/private/dat.gui.min.js:33`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `frontend/src/assets/private/dat.gui.min.js:39`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `frontend/src/assets/private/dat.gui.min.js:44`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `frontend/src/assets/private/dat.gui.min.js:48`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `frontend/src/assets/private/dat.gui.min.js:55`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---
### [!] innerHTML assignment
- **File:** `frontend/src/assets/private/stats.min.js:3`
- **Severity:** MEDIUM
**Problem:** Assigning to innerHTML with unsanitized data is DOM XSS.
**Fix:** Use textContent or a sanitizer (DOMPurify).
---

<details>
<summary>Informational findings (60) — TODOs, debug prints, minor notes</summary>

| File | Issue |
|------|-------|
| `server.ts:19` | Unresolved TODO/FIXME |
| `server.ts:22` | Unresolved TODO/FIXME |
| `server.ts:29` | Unresolved TODO/FIXME |
| `server.ts:175` | Unresolved TODO/FIXME |
| `server.ts:243` | Unresolved TODO/FIXME |
| `server.ts:261` | Unresolved TODO/FIXME |
| `server.ts:335` | Unresolved TODO/FIXME |
| `data/datacache.ts:14` | Unresolved TODO/FIXME |
| `data/datacreator.ts:38` | Unresolved TODO/FIXME |
| `data/datacreator.ts:122` | Unresolved TODO/FIXME |
| `data/datacreator.ts:448` | Unresolved TODO/FIXME |
| `data/mongodb.ts:6` | Unresolved TODO/FIXME |
| `routes/2fa.ts:43` | Unresolved TODO/FIXME |
| `routes/b2bOrder.ts:8` | Unresolved TODO/FIXME |
| `routes/chat.ts:99` | Unresolved TODO/FIXME |
| `routes/chat.ts:156` | Unresolved TODO/FIXME |
| `routes/profileImageUrlUpload.ts:20` | Unresolved TODO/FIXME |
| `routes/showProductReviews.ts:16` | Unresolved TODO/FIXME |
| `routes/userProfile.ts:59` | Unresolved TODO/FIXME |
| `routes/verify.ts:101` | Unresolved TODO/FIXME |
| `routes/verify.ts:107` | Unresolved TODO/FIXME |
| `frontend/src/hacking-instructor/challenges/bonusPayload.ts:21` | Unresolved TODO/FIXME |
| `frontend/src/hacking-instructor/challenges/codingChallenges.ts:20` | Unresolved TODO/FIXME |
| `frontend/src/hacking-instructor/challenges/loginJim.ts:22` | Unresolved TODO/FIXME |
| `frontend/src/assets/private/dat.gui.min.js:59` | Unresolved TODO/FIXME |
| `frontend/src/app/contact/contact.component.spec.ts:168` | Unresolved TODO/FIXME |
| `frontend/src/app/password-strength/password-strength.component.spec.ts:39` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:63` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:66` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:72` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:75` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:81` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:84` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:104` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:127` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:135` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:138` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:141` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:147` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:150` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:156` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:159` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:165` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:171` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:177` | Unresolved TODO/FIXME |
| `frontend/src/app/score-board/helpers/challenge-filtering.spec.ts:183` | Unresolved TODO/FIXME |
| `frontend/src/app/chatbot/chat-conversation/chat-conversation.component.spec.ts:196` | Unresolved TODO/FIXME |
| `frontend/src/app/chatbot/chat-conversation/chat-conversation.component.spec.ts:211` | Unresolved TODO/FIXME |
| `data/static/codefixes/adminSectionChallenge_1_correct.ts:2` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotGreedyInjectionChallenge_1.ts:17` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotGreedyInjectionChallenge_1.ts:72` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotGreedyInjectionChallenge_2_correct.ts:18` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotGreedyInjectionChallenge_2_correct.ts:73` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotGreedyInjectionChallenge_3.ts:18` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotGreedyInjectionChallenge_3.ts:73` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotGreedyInjectionChallenge_3.ts:95` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotGreedyInjectionChallenge_4.ts:18` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotGreedyInjectionChallenge_4.ts:73` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotPromptInjectionChallenge_2_correct.ts:5` | Unresolved TODO/FIXME |
| `data/static/codefixes/chatbotPromptInjectionChallenge_2_correct.ts:18` | Unresolved TODO/FIXME |

</details>


---
*Generated by BugHunter*