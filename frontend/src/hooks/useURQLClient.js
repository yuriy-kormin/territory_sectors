import {cacheExchange, Client, fetchExchange} from "urql";
import {devtoolsExchange} from "@urql/devtools";
import {useEffect, useMemo, useState} from "react";
import {useSelector} from "react-redux";
import {getUserIsLogin} from "../store/selectors/getUser";
import AuthEx, {defExchanges, isLoginExchanges} from "./authEx";

export const useURQLClient = () =>{
    const backendUrl = process.env.REACT_APP_BACKEND_URL
    const [exchanges,setExchanges] = useState(defExchanges)
    const URQLclient = new Client({
        url: backendUrl,
        exchanges: exchanges,
    })

    return URQLclient
}
