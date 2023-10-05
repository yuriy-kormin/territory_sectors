import React, {useState} from 'react';
import {authExchange} from "@urql/exchange-auth";
import {getTokensFromStorage} from "../store/tokenStore";
import {userLogout, userSetAction} from "../store/UserReducer";
import {IsTimemarkValid} from "../api-helpers/lib";
import {RefreshTokenMUTATION} from "../api-helpers/queries/userQueries";
import {useDispatch, useSelector} from "react-redux";
import {getUser,getUserIsLogin} from "../store/selectors/getUser";
import {devtoolsExchange} from "@urql/devtools";
import {cacheExchange, fetchExchange} from "urql";



const AuthEx = async ({ client, forward }) => {
    const user = useSelector(getUser);
    const userIsLogin = useSelector(getUserIsLogin);
    const [refreshState, setRefreshState] = useState(false)
    const dispatch = useDispatch()

    if (!userIsLogin) {
        const tokenData = getTokensFromStorage();
        console.log('tokendata is', tokenData)
        if (tokenData) {
            console.log('tokens found');
            dispatch(userSetAction(tokenData))
            //     return tokenData;
            // } else {
            console.log('token not found');
            return operations$ => {
                const operationResult$ = forward(operations$);
                return operationResult$;
            };
        }
        // }
        // console.log('user is',user)

        return authExchange(
        async utils => {
                console.log('begin getAuth');

                // console.log('user is ', user)

                // if (!user.is_login) {
                //     console.log('try to get tokens');
                //     const tokens = getTokensFromStorage();
                //     if (tokens) {
                //         console.log('tokens found');
                //         dispatch(userSetAction(tokens))
                //         return tokens;
                //     }
                //     console.log('token not found');
                // }

                return {
                    addAuthToOperation: operation => {

                        // const [refreshState, setRefreshState] = useState(false)
                        console.log('begin addAuthToOperation');
                        if (user.is_login && !refreshState) {
                            console.log('set token to headers')
                            return utils.appendHeaders(operation, {
                                Authorization: `Bearer ${user.token}`,
                            })
                        }
                        return operation
                    },
                    willAuthError: () => {
                        console.log('begin willAuthError');
                        if (IsTimemarkValid(user.tokenExpiresIn)) {
                            console.log('token still valid');
                            return false;
                        }

                        if (IsTimemarkValid(user.refreshExpiresIn)) {
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
                            RefreshTokenMUTATION, variables
                        )

                        dispatch(userSetAction({
                            ...user,
                            ...refreshResult.data.refreshToken
                        }))
                        setRefreshState(false);

                    }
                }
            }
        )
    }
}


export const Exchanges = [
            devtoolsExchange,
            cacheExchange,
            AuthEx,
            fetchExchange,
        ]


export default AuthEx;

