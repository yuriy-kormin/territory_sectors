import {useMutation, useQuery} from "urql";

const getExchangeHook = (query)=>{
    const operation = query?.definitions[0]?.operation || ''
    switch (operation) {
        case "mutation":
            return useMutation
        case "query":
            return useQuery
        default:
            throw new Error('Invalid operation type');
    }

}


export const useBackendExchange = (query) => {
    const exchangeHook = getExchangeHook(query)
    return exchangeHook(query)[1]
}