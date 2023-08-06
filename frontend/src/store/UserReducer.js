const setUser = "SET_USER"
const logout = "LOGOUT"

export const userReducer = (state = {is_login:false}, action) =>{
    switch (action.type) {
        case setUser:
            return {...state,is_login: true, ...action.payload}
        case logout:
            return {is_login: false}
        default:
            return state
    }
}

export const userSetAction = payload => ({type:setUser,payload:payload})
export const userLogout = () => ({type:logout})
