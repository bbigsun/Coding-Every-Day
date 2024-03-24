# HTML



- HTML/CSS： https://www.bookstack.cn/read/liyanhui-html-css/3.md
- HTML： https://www.runoob.com/html/html-tutorial.html
- HTML： https://www.runoob.com/tags/tag-progress.html



## HTML 简介

超文本标记语言（HyperText Markup Language，简称：HTML）是一种用于创建网页的标准标记语言。

### HTML 实例

```html
<!DOCTYPE html>
<html>
<head>
    <meta chaset="utf-8">
    <title>Hello HTML</title>
</head>
<body>
    <h1>我的第一个标题</h1>
    <p>我的第一个段落</p>
</body>
</html>
```

实例解析：

![](./images/html%E5%AE%9E%E4%BE%8B.jpg)

**1.Doctype**

文档类型声明（Document Type Declaration，也称 Doctype）。它主要告诉浏览器所查看的文件类型。 在以往的 HTML4.01 和 XHTML1.0 中， 它表示具体的 HTML 版本和风格。而如今 HTML5 不需要表示版本和风格了。

```
<!DOCTYPE html> //不分区大小写
```

**2.html 元素**

首先，元素就是标签的意思，html 元素即 html 标签。html 元素是文档开始和结尾的元素。它是一个双标签，头尾呼应，包含内容。这个元素有一个属性和值：lang="zh-cn"，表示文档采用语言为：简体中文。

```
<html lang="zh-cn"> //如果是英文则为 en
```

**3.head 元素**

用来包含元数据内容，元数据包括：`<link>`、`<meta>`、`<noscript>`、`<script>`、`<style>`、`<title>`。这些内容用来浏览器提供信息，比如 link 提供 CSS 信息，script提供 JavaScript 信息，title 提供页面标题等。

```
<head>...</head> //这些信息在页面不可见
```

**4.meta 元素**

这个元素用来提供关于文档的信息，起始结构有一个属性为：charset="utf8"。表示告诉浏览器页面采用的什么编码，一般来说我们就用 utf8。当然，文件保存的时候也是utf8，而浏览器也设置 utf8 即可正确显示中文。

```
<meta charset="utf-8"> //除了设置编码，还有别的
```

**5.title 元素**

这个元素很简单，顾名思义：设置浏览器左上角的标题。

```
<title>基本结构</title>
```

**6.body 元素**

用来包含文档内容的元素，也就是浏览器可见区域部分。所有的可见内容，都应该在这个元素内部进行添加。

```
<body>...</body>
```

**7.a 元素**

一个超链接，后面会详细探讨。

```
 复制代码<a href="http://www.baidu.com">百度</a>
```

### HTML 标签

HTMl 标记标签通常被称为 HTML 标签（HTML tag）

- HTML 标签是由尖括号包围的关键词，比如 `<html>`
- HTML 标签通常是成对出现的，比如 `<b>` 和 `</b>`
- 标签对中的第一个标签是开始标签，第二个标签是结束标签
- 开始和结束标签也被称为开放标签和闭合标签

### HTML 元素

“HTML 标签” 和 “HTML 元素” 通常都是描述同样的意思。

但严格来讲，一个 HTML 元素包含了开始标签和结束标签。

即，HTML 元素应该是多个标签组成的。

## HTML 编辑器

- VS Code：https://code.visualstudio.com/
- Sublime Text：http://www.sublimetext.com/
- 在线编辑器：https://www.jyshare.com/front-end/61/

## HTML 基础

### 文本元素

| 元素名称 | 说明                                        |
| :------- | :------------------------------------------ |
| a        | 生成超链接                                  |
| br       | 强制换行                                    |
| wbr      | 可安全换行                                  |
| b        | 标记一段文字但不强调                        |
| strong   | 表示重要                                    |
| i        | 表示外文或科学术语                          |
| em       | 表示强调                                    |
| code     | 表示计算机代码                              |
| var      | 表示程序输出                                |
| samp     | 表示变量                                    |
| kbd      | 表示用户输入                                |
| abbr     | 表示缩写                                    |
| cite     | 表示其他作品的标题                          |
| del      | 表示被删除的文字                            |
| s        | 表示文字已不再确认                          |
| dfn      | 表示术语定义                                |
| mark     | 表示与另一段上下文有关的内容                |
| q        | 表示引自他处的内容                          |
| rp       | 与 ruby 元素结合使用，标记括号              |
| rt       | 与 ruby 元素结合使用，标记括号              |
| ruby     | 表示位于表意文字上方或右方的注音符号        |
| bdo      | 控制文字的方向                              |
| small    | 表示小号字体内容                            |
| sub      | 表示下标字体                                |
| sup      | 表示上标字体                                |
| time     | 表示时间或日期                              |
| u        | 标记一段文字但不强调                        |
| span     | 通用元素，没有任何语义。一般配合 CSS 修饰。 |

### 分组元素

| 元素名称   | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| p          | 表示段落                                                     |
| div        | 一个没有任何语义的通用元素，和 span 是对应元素               |
| blockquote | 表示引自他出的大段内容                                       |
| pre        | 表示其格式应被保留的内容                                     |
| hr         | 表示段落级别的主题转换，即水平线                             |
| ul,ol      | 表示无序列表，有序列表                                       |
| li         | 用于 ul,ol 元素中的列表项                                    |
| dl,dt,dd   | 表示包含一系列术语和定义说明的列表。dt 在 dl 内部表示术语，一般充当标题；dd 在 dl 内部表示定义，一般是内容。 |
| figure     | 表示图片                                                     |
| figcaption | 表示 figure 元素的标题                                       |

### 表格元素

| **元素名称** | **说明**         |
| :----------- | :--------------- |
| table        | 表示表格         |
| thead        | 表示标题行       |
| tbody        | 表示表格主体     |
| tfoot        | 表示表脚         |
| tr           | 表示一行单元格   |
| th           | 表示标题行单元格 |
| td           | 表示单元格       |
| col          | 表示一列         |
| colgroup     | 表示一组列       |
| caption      | 表示表格标题     |

### 文档元素

| **元素名称** | **说明**                                        |
| :----------- | :---------------------------------------------- |
| h1~h6        | 表示标题                                        |
| header       | 表示首部                                        |
| footer       | 表示尾部                                        |
| nav          | 表示有意集中在一起的导航元素                    |
| section      | 表示重要概念或主题                              |
| article      | 表示一段独立的内容                              |
| address      | 表示文档或 article 的联系信息                   |
| aside        | 表示与周边内容少有牵涉的内容                    |
| hgroup       | 将一组标题组织在一起                            |
| details      | 生成一个区域，用户将其展开可以获得更多细节      |
| summary      | 用在 details 元素中，表示该元素内容的标题或说明 |

### 嵌入元素

| **元素名称** | **说明**                               |
| :----------- | :------------------------------------- |
| img          | 嵌入图片                               |
| map          | 定义客户端分区响应图                   |
| area         | 表示一个用户客户端分区响应图的区域     |
| audio        | 表示一个音频资源                       |
| video        | 表示一个视频资源                       |
| iframe       | 嵌入一个文档                           |
| embed        | 用插件在 HTML 中嵌入内容               |
| canvas       | 生成一个动态的图形画布                 |
| meter        | 嵌入数值在许可值范围背景中的图形表示   |
| object       | 在 HTML 文档中嵌入内容                 |
| param        | 表示将通过 object 元素传递给插件的参数 |
| progress     | 嵌入目标进展或任务完成情况的图形表示   |
| source       | 表示媒体资源                           |
| svg          | 表示结构化矢量内容                     |
| track        | 表示媒体的附加轨道（例如字幕）         |

### 音频和视频

video 视频元素

| **属性名称** | **说明**                     |
| :----------- | :--------------------------- |
| src          | 视频资源的 URL               |
| width        | 视频宽度                     |
| height       | 视频高度                     |
| autoplay     | 设置后，表示立刻开始播放视频 |
| preload      | 设置后，表示预先载入视频     |
| controls     | 设置后，表示显示播放控件     |
| loop         | 设置后，表示反复播放视频     |
| muted        | 设置后，表示视频处于静音状态 |
| poster       | 指定视频数据载入时显示的图片 |

audio 音频元素

| **属性名称** | **说明**                     |
| :----------- | :--------------------------- |
| src          | 视频资源的 URL               |
| autoplay     | 设置后，表示立刻开始播放视频 |
| preload      | 设置后，表示预先载入视频     |
| controls     | 设置后，表示显示播放控件     |

### 表单元素

在 HTML5 的表单中，提供了各种可供用户输入的表单控件。如下：

| **元素名称** | **说明**                                     |
| :----------- | :------------------------------------------- |
| form         | 表示 HTML 表单                               |
| input        | 表示用来收集用户输入数据的控件               |
| textarea     | 表示可以输入多行文本的控件                   |
| select       | 表示用来提供一组固定的选项                   |
| option       | 表示提供提供一个选项                         |
| optgroup     | 表示一组相关的 option 元素                   |
| button       | 表示可用来提交或重置的表单按钮（或一般按钮） |
| datalist     | 定义一组提供给用户的建议值                   |
| fieldset     | 表示一组表单元素                             |
| legend       | 表示 fieldset 元素的说明性标签               |
| label        | 表示表单元素的说明标签                       |
| output       | 表示计算结果                                 |

1、`<form>` 元素的可用属性如下：

| **元素名称** | **说明**                                                     |
| :----------- | :----------------------------------------------------------- |
| action       | 表示表单提交的页面                                           |
| method       | 表示表单的请求方式：有 POST 和 GET 两种，默认 GET            |
| enctype      | 表示浏览器对发送给服务器的数据所采用的编码格式。有三种：application/x-www-form-urlencoded（默认编码，不能将文件上传到服务器）、multipart/form-data（用于上传文件到服务器）、text/plain（未规范的编码，不建议使用，不同浏览器理解不同） |
| name         | 设置表单名称，以便程序调用                                   |
| target       | 设置提交时的目标位置：_blank、_parent、_self、_top           |
| autocomplete | 设置浏览器记住用户输入的数据，实现自动完成表单。默认为 on 自动完成，如果不想自动完成则设置 off。 |
| novalidate   | 设置是否执行客户端数据有效性检查，后面课程讲解。             |

//使用 get 提交数据

```html
method="get"
```

//丧失自动提示功能

```html
autocomplete="off"
```

//使用_blank 新建目标

```html
target="_blank"
```

2、`<input>`表示用户输入数据

```html
<input name="user">
```

解释：`<input>`元素默认情况会出现一个单行文本框，有五个属性。

| **属性名称** | **说明**                                       |
| :----------- | :--------------------------------------------- |
| autofocus    | 让光标聚焦在某个 input 元素上，让用户直接输入  |
| disabled     | 禁用 input 元素                                |
| autocomplete | 单独设置 input 元素的自动完成功能              |
| form         | 让表单外的元素和指定的表单挂钩提交             |
| type         | input 元素的类型，内容较多，将在下节课展开讲解 |
| name         | 定义 input 元素的名称，以便接收到相应的值      |

//聚焦光标

```
<input name="user" autofocus>
```

//禁用 input

```
<input name="user" disabled>
```

//禁止自动完成

```
<input name="user" autocomplete="off">
```

//表单外的 input

```
<form method="get" id="register"> ... </form><input name="email" form="register">
```

**4.<fieldset>\****对表单进行编组**

```
<fieldset>...</fieldset>
```

解释：<fieldset>元素可以将一些表单元素组织在一起，形成一个整体。

| **属性名称** | **说明**                 |
| :----------- | :----------------------- |
| name         | 给分组定义一个名称       |
| form         | 让表单外的分组与表单挂钩 |
| disabled     | 禁用分组内的表单         |

**5.<legend>\****添加分组说明标签**

```
<fieldset>    <legend> 注册表单 </legend></fieldset>
```

解释：<legend>元素给分组加上一个标题。

**6.<button>\****添加按钮**

```
<button type="submit"></button>
```

解释：<button>元素添加一个按钮，type 属性有如下几个值：

| **值名称** | **说明**                           |
| :--------- | :--------------------------------- |
| submit     | 表示按钮的作用是提交表单，默认     |
| reset      | 表示按钮的作用是重置表单           |
| button     | 表示按钮为一般性按钮，没有任何作用 |

//提交表单

```
<button type="submit">提交</button>
```

//重置表单

```
<button type="reset">重置</button>
```

//普通按钮

```
<button type="button">按钮</button>
```

对于 type 属性为 submit 时，按钮还会提供额外的属性。

| **属性名称**   | **说明**                         |
| :------------- | :------------------------------- |
| form           | 指定按钮关联的表单               |
| formaction     | 覆盖 form 元素的 action 属性     |
| formenctype    | 覆盖 form 元素的 enctype 属性    |
| formmethod     | 覆盖 form 元素的 method 属性     |
| formtarget     | 覆盖 form 元素的 target 属性     |
| formnovalidate | 覆盖 form 元素的 novalidate 属性 |

//表单外关联提交

```
<button type="submit" form="register">提交</button>
```



**一．\****type***\* 属性总汇**

input 元素可以用来生成一个供用户输入数据的简单文本框。在默认的情况下，什么样的数据均可以输入。而通过不同的属性值，可以限制输入的内容。

| **属性名称**                                      | **说明**                                       |
| :------------------------------------------------ | :--------------------------------------------- |
| text                                              | 一个单行文本框，默认行为                       |
| password                                          | 隐藏字符的密码框                               |
| search                                            | 搜索框，在某些浏览器键入内容会出现叉标记取消   |
| submit、reset、button                             | 生成一个提交按钮、重置按钮、普通按钮           |
| number、range                                     | 只能输入数值的框；只能输入在一个数值范围的框   |
| checkbox、radio                                   | 复选框，用户勾选框；单选框，只能在几个中选一个 |
| image、color                                      | 生成一个图片按钮，颜色代码按钮                 |
| email、tel、url                                   | 生成一个检测电子邮件、号码、网址的文本框       |
| date、month、time、week、datetime、datetime-local | 获取日期和时间                                 |
| hidden                                            | 生成一个隐藏控件                               |
| file                                              | 生成一个上传控件                               |

**二．\****input***\* 元素解析**

***\*1.type\**** 为 ***\*text\**** 值时****

```
<input type="text">
```

解释：当 type 值为 text 时，呈现的就是一个可以输入任意字符的文本框，这也是默认行为。并且，还提供了一些额外的属性。

| **属性名称** | **说明**                                                     |
| :----------- | :----------------------------------------------------------- |
| list         | 指定为文本框提供建议值的 datalist 元素，其值为datalist 元素的 id 值 |
| maxlength    | 设置文本框最大字符长度                                       |
| pattern      | 用于输入验证的正则表达式                                     |
| placeholder  | 输入字符的提示                                               |
| readonly     | 文本框处于只读状态                                           |
| disabled     | 文本框处于禁用状态                                           |
| size         | 设置文本框宽度                                               |
| value        | 设置文本框初始值                                             |
| required     | 表明用户必须输入一个值，否则无法通过输入验证                 |

//设置文本框长度

```
<input type="text" size="50">
```

//设置文本框输入字符长度

```
<input type="text" maxlength="10">
```

//设置文本框的初始值

```
<input type="text" value="初始值">
```

//设置文本框输入提示

```
<input type="text" placeholder="请输入内容">
```

//设置文本提供的建议值

```
<input list="footlist"><datalist id="footlist">    <option value="苹果">苹果</option>    <option value="桔子">桔子</option>    <option value="香蕉" label="香蕉">    <option value="梨子"></datalist>
```

//设置文本框内容为只读，可以提交数据

```
<input type="text" readonly>
```

//设置文本框内容不可用，不可以提交数据

```
<input type="text" disabled>
```

**2.type\****为***\* password值时**

```
<input type="password">
```

解释：当 type 值为 password 时，一般用于密码框的输入，所有的字符都会显示星号。密码框也有一些额外属性。

| **属性名称** | **说明**                 |
| :----------- | :----------------------- |
| maxlength    | 设置密码框最大字符长度   |
| pattern      | 用于输入验证的正则表达式 |
| placeholder  | 输入密码的提示           |
| readonly     | 密码框处于只读状态       |
| disabled     | 文本框处于禁用状态       |
| size         | 设置密码框宽度           |
| value        | 设置密码框初始值         |
| required     | 表明用户必须输入同一个值 |

这里除了正则和验证需要放在下一节，其余和文本框一致。

**3.type\****为***\* search时**

```
<input type="search">
```

解释：和文本框一致，在除 Firefox 浏览器的其他现代浏览器，会显示一个叉来取消搜索内容。额外属性也和 text 一致。

**4.type\****为***\* number****、****range时**

```
<input type="number"><input type="range">
```

解释：只限输入数字的文本框，不同浏览器可能显示方式不同。生成一个数值范围文本框，只是样式是拖动式。额外属性如下：

| **属性名称** | **说明**                                                     |
| :----------- | :----------------------------------------------------------- |
| list         | 指定为文本框提供建议值的 datalist 元素，其值为datalist 元素的 id 值 |
| min          | 设置可接受的最小值                                           |
| max          | 设定可接受的最大值                                           |
| readonly     | 设置文本框内容只读                                           |
| required     | 表明用户必须输入一个值，否则无法通过输入验证                 |
| step         | 指定上下调节值的步长                                         |
| value        | 指定初始值                                                   |

//范围和步长

```
<input type="number" step="2" min="10" max="100">
```

**5.type\****为***\* date系列时**

```
<input type="date"><input type="month"><input type="time"><input type="week"><input type="datetime"><input type="datetime-local">
```

解释：实现文本框可以获取日期和时间的值，但支持的浏览器不完整。我们测试 Chrome 和 Opera 支持，其他浏览器尚未支持。所以，在获取日期和时间，目前还是推荐使用 jQuery 等前端库来实现日历功能。额外属性和 number 一致。

**6.type\****为***\* color时**

```
<input type="color">
```

解释：实现文本框获取颜色的功能，最新的现代浏览器测试后 IE 不支持，其余的都能显示一个颜色对话框提供选择。

**7.type\****为***\* checkbox****、****radio时**

```
音乐<input type="checkbox"> 体育<input type="checkbox"><input type="radio" name="sex" value="男"> 男 <input type="radio" name="sex" value="女"> 女
```

解释：生成一个获取布尔值的复选框或固定选项的单选框。额外属性如下：

| **属性名称** | **说明**                                          |
| :----------- | :------------------------------------------------ |
| checked      | 设置复选框、单选框是否为勾选状态                  |
| required     | 表示用户必须勾选，否则无法通过验证                |
| value        | 设置复选框、单选框勾选状态时提交的数据。默认为 on |

//默认勾选，默认值为 1

```
<input type="checkbox" name="music" checked value="1">
```

**8.type\****为***\* submit****、****reset和\**** button***\*时**

```
<input type="submit">
```

解释：生成一个按钮，三种模式：提交、重置和一般按钮，和<button>元素相同。

| **值名称** | **说明**         |
| :--------- | :--------------- |
| submit     | 生成一个提交按钮 |
| reset      | 生成一个重置按钮 |
| button     | 生成一个普通按钮 |

如果是 submit 时，还提供了和<button>元素一样的额外属性：formaction、formenctype、formmethod、formtarget 和 formnovalidate。

**9.type\****为***\* image时**

```
<input type="image" src="img.png">
```

解释：生成一个图片按钮，点击图片就实现提交功能，并且传送了分区响应数据。图片按钮也提供了一些额外属性。

| **属性名称** | **说明**                                                     |
| :----------- | :----------------------------------------------------------- |
| src          | 指定要显示图像的 URL                                         |
| alt          | 提供图片的文字说明                                           |
| width        | 图像的长度                                                   |
| height       | 图像的高度                                                   |
| 提交额外属性 | formaction、formenctype、formmethod、formtarget和 formnovalidate。 |

**10.type\****为***\* email****、****tel****、****url时**

```
<input type="email"><input type="tel"><input type="url">
```

解释：email 为电子邮件格式、tel 为电话格式、url 为网址格式。额外属性和 text 一致。但对于这几种类型，浏览器支持是不同的。email 支持比较好，现在浏览器都支持格式验证；tel 基本不支持；url 支持一般，部分浏览器只要检测到 [http://就能通过。](http://xn--xft496fsekqja./)

**11.type\****为***\* hidden时**

```
<input type="hidden">
```

解释：生成一个隐藏控件，一般用于表单提交时关联主键 ID 提交，而这个数据作为隐藏存在。

**12.type\****为***\* file时**

```
<input type="file">
```

解释：生成一个文件上传控件，用于文件的上传。额外提供了一些属性：

| **属性名称** | **说明**                                 |
| :----------- | :--------------------------------------- |
| accept       | 指定接受的 MIME 类型                     |
| required     | 表明用户必须提供一个值，否则无法通过验证 |

```
 复制代码accept="image/gif, image/jpeg, image/png"
```

**一．其他元素**

表单元素还剩下几个元素没有讲解，包括下拉框列表 select、多行文本框 textarea、和 output 计算结果元素。

| **元素名称** | **说明**                 |
| :----------- | :----------------------- |
| select       | 生成一个下拉列表进行选择 |
| optgroup     | 对 select 元素进行编组   |
| option       | select 元素中的项目      |
| textarea     | 生成一个多行文本框       |
| output       | 表示计算结果             |

**1.\****生成下拉列表**

```
<select name="fruit">　　<option value="1">苹果</option>　　&lt;option value="2"&gt;橘子&lt;/option&gt;　　&lt;option value="3"&gt;香蕉&lt;/option&gt;&lt;/select&gt;
```

解释：<select>下拉列表元素至少包含一个<option>子元素，才能形成有效的选项列表。<select>元素包含两个子元素<option>项目元素和<optgroup>分组元素，还包含了一些额外属性。

| **属性名称** | **说明**                         |
| :----------- | :------------------------------- |
| name         | 设定提交时的名称                 |
| disabled     | 将下拉列表禁用                   |
| form         | 将表单外的下拉列表与某个表单挂钩 |
| size         | 设置下拉列表的高度               |
| multiple     | 设置是否可以多选                 |
| autofocus    | 获取焦点                         |
| required     | 选择验证，设置后必须选择才能通过 |

//设置高度并实现多选

```
<select name="fruit" size="30" multiple>
```

//默认首选

```
<option value="2" selected>橘子</option>
```

//使用 optgroup 进行分组，label 为分组名称，disabled 可以禁用分组

```
<optgroup label="水果类">    <option value="1">苹果</option>    <option value="2" selected>橘子</option>    <option value="3" label="香蕉">香蕉</option></optgroup>
```

**2.\****多行文本框**

```
<textarea name="content">请留下您的建议！ </textarea>
```

解释：生成一个可变更大小的多行文本框。属性如下：

| **属性名称** | **说明**                                 |
| :----------- | :--------------------------------------- |
| name         | 设定提交时的名称                         |
| form         | 将表单外的多行文本框与某个表单挂钩       |
| readonly     | 设置多行文本框只读                       |
| disabled     | 将多行文本框禁用                         |
| maxlength    | 设置最大可输入的字符长度                 |
| autofocus    | 获取焦点                                 |
| placeholder  | 设置输入时的提示信息                     |
| rows         | 设置行数                                 |
| cols         | 设置列数                                 |
| wrap         | 设置是否插入换行符，有 soft 和 hard 两种 |
| required     | 设置必须输入值，否则无法通过验证         |

//设置行高和列宽，设置插入换行符

```
<textarea name="content" rows="20" cols="30" wrap="hard"></textarea>
```

3.计算结果

```
<form oninput="res.value = num1.valueAsNumber * num2.valueAsNumber">    <input type="number" id="num1"> x <input type="number" id="num2">    <output for="num1 num2" name="res"></form>
```

解释：output 就是计算两个文本框之间的值，其实就是内嵌了 JavaScript 功能。

**二．输入验证**

HTML5 对表单提供了输入验证检查方式，但这种验证还是比较简陋的，并且不同的浏览器支持的成熟度还不同。在大部分情况下，可能还是要借助 jQuery 等前端库来实现丰富的验证功能和显示效果。

//必须填写一个值

```
<input type="text" required>
```

//限定在某一个范围内

```
<input type="number" min="10" max="100">
```

//使用正则表达式

```
<input type="text" placeholder="请输入区号+座机" required pattern="^[\d]{2,4}\-[\d]{6,8}$">
```

//禁止表单验证

```
<form action="http://li.cc" novalidate>
```

### 全部属性和其他

**一．实体**

HTML 实体就是将有特殊意义的字符通过实体代码显示出来。

![第 11 章 全局属性和其他  - 图1](https://static.bookstack.cn/projects/liyanhui-html-css/5c46cdd3d06cb3e2627501d4e929fea3.png)

**二．元数据**

<meta>元素可以定义文档中的各种元数据，而且一个 HTML 页面可以包含多个<meta>元素。

**1.\****指定名***\*/\****值元数据对**

```
<meta name="author" content="bnbbs"><meta name="description" content="这是一个 HTML5 页面">&lt;meta name="keywords" content="html5,css3,响应式"&gt;&lt;meta name="generator" content="sublime text 3"&gt;
```

| **元数据名称** | **说明**           |
| :------------- | :----------------- |
| author         | 当前页面的作者     |
| description    | 当前页面的描述     |
| keywords       | 当前页面的关键字   |
| generator      | 当前页面的编码工具 |

**2.声明字符编码**

```
<meta charset="utf-8">
```

**3.模拟 HTTP 标头字段**

//5 秒跳转到指定 URL

```
<meta http-equiv="refresh" content="5;http://li.cc">
```

//另一种声明字符编码

```
<meta http-equiv="content-type" content="text/html charset=utf-8">
```

| **属性值**   | **说明**                                   |
| :----------- | :----------------------------------------- |
| refresh      | 重新载入当前页面，或指定一个 URL。单位秒。 |
| content-type | 另一种声明字符编码的方式                   |

**三．全局属性**

在此之前，我们涉及到的元素都讲解了它的局部数据，当然也知道一些全局属性，比如id。全局属性是所有元素共有的行为，HTML5 还提供了一些其他的全局属性。

**1.id\****属性**

```
<p id="abc">段落</p>
```

解释：id 属性给元素分配一个唯一标识符。这种标识符通常用来给 CSS 和 JavaScript 调用选择元素。一个页面只能出现一次同一个 id 名称。

**2.class\****属性**

```
<p class="abc">段落</p>&lt;p class="abc"&gt;段落&lt;/p&gt;&lt;p class="abc"&gt;段落&lt;/p&gt;
```

解释：class 属性用来给元素归类。通过是文档中某一个或多个元素同时设置 CSS 样式。

**3.accesskey\****属性**

```
<input type="text" name="user" accesskey="n">
```

解释：快捷键操作，windows 下 alt+指定键，前提是浏览器 alt 并不冲突。

**4.contenteditable\****属性**

```
<p contenteditable="true">我可以修改吗</p>
```

解释：让文本处于可编辑状态，设置 true 则可以编辑，false 则不可编辑。或者直接设置属性。

**5.dir\****属性**

```
<p dir="rtl">文字到右边了</p>
```

解释：让文本从左到右（ltr），还是从右到左（rtl）。

**6.hidden\****属性**

```
<p hidden>文字到右边了</p>
```

解释：隐藏元素。

**7.lang\****属性**

```
<p lang="en">HTML5</p>
```

解释：可以局部设置语言。

**8.title\****属性**

```
<p title="HTML5 教程">HTML5</p>
```

解释：对元素的内容进行额外的提示。

**9.tabindex\****属性**

```
<input type="text" name="user" tabindex="2">&lt;input type="text" name="user" tabindex="1"&gt;
```

解释：表单中按下 tab 键，实现获取焦点的顺序。如果是-1，则不会被选中。

**10.style\****属性**

```
<p style="color:red;">CSS 样式</p>
```

解释：设置元素行内 CSS 样式。





## HTML 练习


| 名称 | 解释 |
|:-----|:-----|
| demo1 | CSS 设置卡片（card）样式 |
| demo2 | HTML/CSS/JS 时间轴 |
| demo3 | CSS loading 效果 |




