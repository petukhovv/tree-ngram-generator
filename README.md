# ast-ngram-generator

N-gram generation by AST.

### Running example

```
python3 main.py ./ast 3 3 ./ngrams
```

### Parameters

- Folder with AST files (with any nesting);
- Max gram order (n in n-gram): grams will be generated that are smaller and equal n;
- Max distance between nodes (which are part of n-gram);
- Output folder (n-gram configurations in JSON format; nesting will be repeated).

### AST format

The program is required on input the AST of the following format (example input):
```
[
   {
      "type":"FUN",
      "chars":"override fun onCreateView(inflater: LayoutInflater?, container: ViewGroup?, savedInstanceState: Bundle?): View? {\n        dialog.window.requestFeature(Window.FEATURE_NO_TITLE)\n\n        DaggerAppComponent.builder()\n                .appModule(AppModule(context))\n                .mainModule((activity.application as MyApplication).mainModule)\n                .build().inject(this)\n\n        var view = inflater?.inflate(R.layout.dialog_signup, container, false)\n\n        ButterKnife.bind(this, view!!)\n\n        return view\n    }",
      "children":[
         {
            "type":"MODIFIER_LIST",
            "chars":"override",
            "children":[
               {
                  "type":"override",
                  "chars":"override"
               }
            ]
         },
         {
            "type":"IDENTIFIER",
            "chars":"onCreateView"
         },
         {
            "type":"VALUE_PARAMETER_LIST",
            "chars":"(inflater: LayoutInflater?, container: ViewGroup?, savedInstanceState: Bundle?)",
            "children":[
               {
                  "type":"LPAR",
                  "chars":"("
               },
               {
                  "type":"VALUE_PARAMETER",
                  "chars":"inflater: LayoutInflater?",
                  "children":[
                     {
                        "type":"IDENTIFIER",
                        "chars":"inflater"
                     }
                  ]
               }
            ]
         }
      ]
   }
]
```
It is Kotlin AST, generated by [**Kotlin custom compiler**](https://github.com/PetukhovVictor/kotlin-academic/tree/vp/ast_printing_text)

Also reqired AST transformer, which is a part of [**github-kotlin-code-collector**](https://github.com/PetukhovVictor/github-kotlin-code-collector) (see `src/lib/helper/AstHelper.py`)

### Output format

N-gram configuration is written in the JSON format.

For example:

```
[
   {
      "type":"ngram",
      "params":{
         "name":"FUN",
         "node_types":[
            "FUN"
         ],
         "max_distance":3
      }
   },
   {
      "type":"ngram",
      "params":{
         "name":"MODIFIER_LIST",
         "node_types":[
            "MODIFIER_LIST"
         ],
         "max_distance":3
      }
   },
   {
      "type":"ngram",
      "params":{
         "name":"FUN:MODIFIER_LIST",
         "node_types":[
            "FUN",
            "MODIFIER_LIST"
         ],
         "max_distance":3
      }
   },
   {
      "type":"ngram",
      "params":{
         "name":"override",
         "node_types":[
            "override"
         ],
         "max_distance":3
      }
   },
   {
      "type":"ngram",
      "params":{
         "name":"MODIFIER_LIST:override",
         "node_types":[
            "MODIFIER_LIST",
            "override"
         ],
         "max_distance":3
      }
   },
   {
      "type":"ngram",
      "params":{
         "name":"FUN:override",
         "node_types":[
            "FUN",
            "override"
         ],
         "max_distance":3
      }
   },
   {
      "type":"ngram",
      "params":{
         "name":"FUN:MODIFIER_LIST:override",
         "node_types":[
            "FUN",
            "MODIFIER_LIST",
            "override"
         ],
         "max_distance":3
      }
   }
]
```

N-gram configuration can be used in [ast2vec](https://github.com/PetukhovVictor/ast2vec).