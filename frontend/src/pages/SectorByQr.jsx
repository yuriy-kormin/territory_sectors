import React, {useState} from 'react';
import {useParams} from "react-router-dom";
import {useBackendExchange} from "../hooks/useBackendExchange";
import {UuidExistQUERY} from "../api-helpers/queries/UuidQueries";
import {parseUuidExchangeResult} from "../api-helpers/lib";
import useFetchResult from "../hooks/useFetchResult";
import {useQuery} from "urql";
import {useDispatch, useSelector} from "react-redux";
import {userAnonSetAction, userSetAction} from "../store/UserReducer";
import {LoginQUERY} from "../api-helpers/queries/userQueries";
import {getUser} from "../store/selectors/getUser";

const SectorByQr = () => {
    const params = useParams()
    const dispatch = useDispatch()
    const user = useSelector(getUser);
    console.log('user is ',user)
    dispatch(userAnonSetAction())
    console.log('user is ',user)

    // // params.sectorId
    // const callback = useBackendExchange(UuidExistQUERY);
    const[{ data, fetching, error }, reexecuteQuery]  = useQuery({
        query:UuidExistQUERY,
        variables:{id:params.sectorId}
    })
    // callback({id:"asdad"})
    // console.log('heloo',callback({id:"asdad"}))
    return (
        <div>
            <h1>
            {/*<h1>{fetching*/}
            {/*    ? "fetch"*/}
            {/*    : data*/}
            {/*}*/}
                dcs {params.sectorId}</h1>
        </div>
    );
};

export default SectorByQr;