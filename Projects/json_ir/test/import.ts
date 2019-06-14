enum Statement {
    ImportModule,
    ImportSymbol,
}

interface ImportModule {
    type: number,
    from: string,
    alias: string
}

const target: ImportModule[] = [
    {
        type: Statement.ImportModule,
        from: "sys.object.ir",
        alias: undefined, //undefined 表示不检查这一项
    }
]
