import NavBar from "./components/NavBar";
import {Provider} from 'urql';
import {useURQLClient} from "./hooks/useURQLClient";
import AppRouter from "./components/AppRouter";


function App({urqlClient=undefined}) {
    const client = useURQLClient()

return (
    <Provider value={urqlClient || client}>
        <div className="App app-container d-flex flex-column vh-100">
            <NavBar />
            <AppRouter />
        </div>
    </Provider>
  );
}

export default App;
