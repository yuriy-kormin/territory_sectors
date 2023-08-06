import {combineReducers} from "redux";
import {userReducer} from "./UserReducer";
import { configureStore } from '@reduxjs/toolkit'


const rootReducer = combineReducers({
    user:userReducer,
})

export const store = configureStore({
    reducer: rootReducer,
    devTools:true,
})
