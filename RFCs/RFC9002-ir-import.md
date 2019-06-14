RFC9002[IR]: Import Modules and Symbols
=======================================

import 是顶级关键词, 不能作为变量名.

import 相关的语义如下:

### ImportModule

导入模块.

### 示例代码

```python
import sys.console
import sys.object.string as str
```

as 表示 alias

### 中间表示

```ts
interface ImportModule {
    type: number,
    from: string,
    alias: string?,
}
```

- `from`: 导入的模块名
- `alias`: 表示别称

### ImportSymbol

导入模块中的某些符号.

#### 示例代码

```python
import sys.object.*
import mxnet with cpu, gpu
import numpy with
       zeros as z, ones as o
       empty
```

* 导入所有符号

with 导入指定的符号

如果很多, 可以换行, 没有规定每行的个数, 但是注意不能空行

换行之后需要有缩进

#### 中间表示

```ts
interface ImportSymbol {
    type: number,
    from: string,
    symbol: bool | string[] | [string, string][],
}
```

- `from`: 导入的模块名
- `symbol: bool`: 是否导入该子模块中所有可见符号
- `symbol: string`: 导入的符号名
- `symbol: [string, string]`: 前一个表示原名, 后一个表示别称
