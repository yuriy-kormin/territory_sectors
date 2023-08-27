export const IsTimemarkValid = (timemark) => {
    const expirationTime = new Date(timemark * 1000);
    const currentTime = new Date();
    return currentTime < expirationTime
}

const getOperationName = gql =>
    gql.definitions[0].selectionSet.selections[0].name.value

const getResponseData = (response) => {
    const opName = getOperationName(response.operation.query)
    if (response.data.hasOwnProperty(opName)) {
        return response.data[opName]
    }
    return undefined;
}

export const parseAuthResult = (response) => {
    const authData = getResponseData(response)
    return {
        token: authData?.token,
        refreshToken: authData?.refreshToken,
        refreshExpiresIn: authData?.refreshExpiresIn,
        username: authData?.payload?.username,
        tokenExpiresIn:authData?.payload?.exp
    }
}

export const parseUuidExchangeResult = (response) => {
    return getResponseData(response)
}