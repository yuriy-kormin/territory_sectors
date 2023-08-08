export const IsTimemarkValid = (timemark) => {
    const expirationTime = new Date(timemark * 1000);
    const currentTime = new Date();
    return currentTime < expirationTime
}

const getOperationName = gql =>
    gql.definitions[0].selectionSet.selections[0].name.value

export const getResponseData = (response) => {
    const opName = getOperationName(response.operation.query)
    if (response.data.hasOwnProperty(opName)) {
        return response.data[opName]
    }
    return undefined;
}