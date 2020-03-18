# ckan-reader

CKAN の WebAPI に参照する wrapper モジュールです

## 実行方法

```
from ckanreader.ckan import RequestV3
from ckanreader.action.domain import Package

req = RequestV3("http://test.example.com")
result = Package.search(req, "平成")
```
