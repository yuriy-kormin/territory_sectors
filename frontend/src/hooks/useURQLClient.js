import {cacheExchange, Client, fetchExchange} from "urql";
import {devtoolsExchange} from "@urql/devtools";
import {useState} from "react";
import {useSelector} from "react-redux";
import {getUser} from "../store/selectors/getUser";
import AuthEx from "./authEx";

export const useURQLClient = () =>{
    const user = useSelector(getUser);
    const backendUrl = process.env.REACT_APP_BACKEND_URL
    const [exchanges,setExchanges] = useState([
            devtoolsExchange,
            cacheExchange,
            fetchExchange,
        ])
    if (user.is_login) {
        setExchanges([
            devtoolsExchange,
            cacheExchange,
            AuthEx,
            fetchExchange,
        ])
    }
    const URQLclient = new Client({
        url: backendUrl,
        exchanges: exchanges
    })

    return URQLclient
}
