import React from 'react';
import {Route, Routes, useNavigate, useParams} from "react-router-dom";
import Start from "../pages/Start";
import SectorByQr from "../pages/SectorByQr";

const AppRouter = () => {
    // const navigate = useNavigate();
    // const QRLENGTH = 10
    // const SectorRouter = () => {
    //   const params = useParams()
    //   if (params.sectorId.length === QRLENGTH) {
    //     return <SectorByQr />;
    //   } else {
    //     navigate('/page-not-found');
    //     return null;
    //   }
    // };
    return (
        <Routes>
            <Route exact path="/" element={<Start />} />
            <Route exact path="/:sectorId" element={<SectorByQr />}/>
            <Route path="/page-not-found" element={<h1>Page Not Found </h1>} />
        </Routes>
        );
};

export default AppRouter;