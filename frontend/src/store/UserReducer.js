import { removeTokensFromStorage, setTokensToStorage } from "./tokenStore";

const SET_USER = "SET_USER";
const SET_STORAGE = "SET_STORAGE";
const LOGOUT = "LOGOUT";

const initialState = {
  is_login: false,
};

export const userReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_USER:
      return { ...state, is_login: true, ...action.payload };
    case SET_STORAGE:
      setTokensToStorage(action.payload);
      return { ...state, is_login: true, ...action.payload };
    case LOGOUT:
      removeTokensFromStorage();
      return { ...initialState };
    default:
      return state;
  }
};

export const userSetAction = (payload) => ({ type: SET_USER, payload });
export const storageSetAction = (payload) => ({ type: SET_STORAGE, payload });
export const userLogout = () => ({ type: LOGOUT });
