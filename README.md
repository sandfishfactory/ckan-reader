# ckan-reader

CKAN の WebAPI に参照する wrapper モジュールです

## 実行方法

```
>>> from ckanreader.ckan import RequestV3
>>> req = RequestV3("https://catalog.data.metro.tokyo.lg.jp")
>>>
>>>
>>> from ckanreader.action.domain import Package
>>> result = Package.search(req, "平成")
```
