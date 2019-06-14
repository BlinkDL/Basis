export enum Tasks {
    ImportModule,
    ImportSymbol,
}

interface ImportModule {
    type: number,
    from: string,
    alias: string
}
interface ImportSymbol {
    type: number,
    from: string,
    symbol: string[] | [string, string][]
}

export {
    ImportModule,
    ImportSymbol,
}
