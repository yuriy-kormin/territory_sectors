import React, {useState} from 'react';
import {authExchange} from "@urql/exchange-auth";
import {getTokensFromStorage} from "../store/tokenStore";
import {userLogout, userSetAction} from "../store/UserReducer";
import {IsTimemarkValid} from "../api-helpers/lib";
import {RefreshTokenMUTATION} from "../api-helpers/queries/userQueries";
import {useDispatch, useSelector} from "react-redux";
import {getUser} from "../store/selectors/getUser";

const AuthEx = () => {
    const user = useSelector(getUser);
    const [refreshState,setRefreshState] = useState(false)
    const dispatch = useDispatch()
    return (
    authExchange(
    async utils => {
        console.log('begin getAuth');
        if (!user.is_login) {
            const tokens = await getTokensFromStorage();
            if (tokens) {
                console.log('tokens found');
                dispatch(userSetAction(tokens))
                return tokens;
            }
            console.log('token not found');
        }
        return {
            addAuthToOperation: operation => {
                console.log('begin addAuthToOperation');
                if (user.is_login && !refreshState){
                    console.log('set token to headers')
                    return utils.appendHeaders(operation,{
                        Authorization: `Bearer ${user.token}`,
                    })
                }
                return operation
            },
            willAuthError: () => {
                console.log('begin willAuthError');
                if (IsTimemarkValid(user.tokenExpiresIn)){
                    console.log('token still valid');
                    return false;
                }

                if (IsTimemarkValid(user.refreshExpiresIn))  {
                    console.log('token was expired  but refresh is active');
                    return true;
                }
                console.log('both token is expired');
                dispatch(userLogout())
            },
            didAuthError: (error, operation) => {
                console.log('begin didAuthError');

                return error.graphQLErrors.some(e => e.extensions?.code === 'FORBIDDEN');
            },
            refreshAuth: async () => {
                console.log('begin refreshAuth');
                setRefreshState(true);
                const variables = {refreshToken: user.refreshToken}
                const refreshResult = await utils.mutate(
                    RefreshTokenMUTATION,variables
                )

                dispatch(userSetAction({
                    ...user,
                    ...refreshResult.data.refreshToken
                }))
                setRefreshState(false);

            }
        }
})
    );
};

export default AuthEx;

