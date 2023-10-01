const KEY_NAME = 'JWT'


export const getTokensFromStorage = () => {
    const data = localStorage.getItem(KEY_NAME);
    if (data) {return JSON.parse(data)}
}

export const setTokensToStorage = async(data) => {
    const json = JSON.stringify(data);
    localStorage.setItem(KEY_NAME, json);
}

export const removeTokensFromStorage = async(data) => {
    localStorage.removeItem(KEY_NAME);
}