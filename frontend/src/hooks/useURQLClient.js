import {cacheExchange, Client, fetchExchange} from "urql";
import {devtoolsExchange} from "@urql/devtools";
import {useEffect, useMemo, useState} from "react";
import {useSelector} from "react-redux";
import {getUserIsLogin} from "../store/selectors/getUser";
import AuthEx, {Exchanges} from "./authEx";

export const useURQLClient = () =>{
    const backendUrl = process.env.REACT_APP_BACKEND_URL
    const [exchanges,setExchanges] = useState(Exchanges)
    const URQLclient = new Client({
        url: backendUrl,
        exchanges: exchanges,
    })

    return URQLclient
}
