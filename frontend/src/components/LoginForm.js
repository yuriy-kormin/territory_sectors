import React, {useRef, useState} from 'react';
import TextInput from "./components/input/TextInput";
import NewButton from "./components/button/NewButton";
import {Form} from "react-bootstrap";
import {useDispatch} from "react-redux";
import {faUser, faLock} from '@fortawesome/free-solid-svg-icons';
import Loading from "./components/spinner/Loading";
import ErrorAlert from "./components/Alert/ErrorAlert";

const LoginForm = () => {
    const dispatch = useDispatch()
    const [loginError, setLoginError] = useState({error: false, message:''});


    const loginInputRef = useRef();
    const passwordInputRef = useRef();

    const submitAction = (e) => {
        e.preventDefault()
        processUserLogin(
            loginInputRef.current.value,
            passwordInputRef.current.value,
            processLogin,
            dispatch
        ).then(loginResult => {
            if (!loginResult.result) {
                setLoginError({error: true, message: loginResult.info.message})
            }
        })
    }

    return (
        <Form className={"mt-5"} data-testid='loginForm'>
            {
                loginError.error && !result.fetching && (
                <ErrorAlert
                    show={loginError}
                    onClose={() => setLoginError(false)}
                >{loginError.message}</ErrorAlert>
                )
            }
            <TextInput
                   id="login_field"
                   label="Login"
                   data-testid='login'
                   icon={faUser}
                   className = {loginError.error && !result.fetching?'is-invalid':''}
                   _ref = {loginInputRef}
                   autoComplete='username'
            />
            <TextInput
                id="password_field"
                label="Password"
                data-testid='password'
                icon={faLock}
                className = {loginError.error && !result.fetching?'is-invalid':''}
                _ref = {passwordInputRef}
                autoComplete='password'
                is_password={true}
            />
            <NewButton
                variant="primary"
                classes={"mt-3"}
                data-testid='login_btn'
                type="submit"
                onClick={submitAction}
                disabled={result.fetching?'disabled':''}
            > {result.fetching ?<Loading />:''}
                {result.fetching?'Loading...':'Login'}</NewButton>
        </Form>
    );
};

export default LoginForm;