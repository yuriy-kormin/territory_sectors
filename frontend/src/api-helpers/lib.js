export const IsTimemarkValid = (timemark) => {
    const expirationTime = new Date(timemark * 1000);
    const currentTime = new Date();
    return currentTime < expirationTime
}

const getOperationName = gql =>
    gql.definitions[0].selectionSet.selections[0].name.value

export const getResponseData = (response) => {
    const keys = Object.keys(response);
    if (keys.length > 0) {
        const firstKey = keys[0];
        return response[firstKey];
    }
    return undefined;
}