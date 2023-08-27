import {useMutation, useQuery} from "urql";

const getExchangeHook = (query)=>{
    const operation = query?.definitions[0]?.operation || ''
    switch (operation) {
        case "mutation":
            return 'mutation'
        case "query":
            return 'query'
        default:
            throw new Error('Invalid operation type');
    }

}


export const useBackendExchange = (query) => {
    const exchangeHook = getExchangeHook(query)
    // console.log('test',exchangeHook)
    const queryHook = useQuery
    switch (exchangeHook) {
        case 'mutation':
            const hook = useMutation
            return hook(query)[1]
        case "query":
            const result = (vars) => {
                return queryHook({
                    query: query,
                    variables: vars,
                    pause: true
                })[0]
            }
            return result
            // return ''
    }
}