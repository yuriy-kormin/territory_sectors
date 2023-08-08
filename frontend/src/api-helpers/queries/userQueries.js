import {gql} from "urql";

export const LoginQUERY =gql`
   mutation TokenAuth($username: String!, $password: String!){
        tokenAuth(username:$username,password:$password){
            token
            refreshToken
            payload
            refreshExpiresIn
        }
    }
`

export const RefreshTokenMUTATION =gql`
    mutation RefreshAuth($refreshToken:String!){
    refreshToken(refreshToken:$refreshToken){
        token
        payload
        refreshToken
        refreshExpiresIn
      }
    }
`