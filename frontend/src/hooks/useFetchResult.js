// import React, {useState} from 'react';
//
// const UseFetchResult = () => {
//     const regexp=/(?<=^\[.*\]\s+)\S.*/gm
//     const [fetchResult, setFetchResult] = useState({
//         fetching:false,
//         error:undefined,
//         result:undefined,
//     });
//     const customSetFetchResult = (fetching,result) =>{
//         return setFetchResult({
//             fetching: fetching,
//             error: regexp.exec(result.error?.message || ''),
//             result: result
//         })
//     }
//     return [fetchResult,customSetFetchResult]
// };
//
// export default UseFetchResult;