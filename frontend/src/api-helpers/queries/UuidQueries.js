import {gql} from "urql";

export const UuidExistQUERY =gql`
    query ($id:String!){
      uuidCheck(id:$id){
            ok
      }
    }
`