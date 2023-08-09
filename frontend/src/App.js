import DivMap from "./components/DivMap";
import {useSelector} from "react-redux";
import {getUser} from "./store/selectors/getUser";
import NavBar from "./components/NavBar";
import LoginForm from "./components/LoginForm";
import {Provider} from 'urql';
import {useURQLClient} from "./hooks/useURQLClient";


function App({urqlClient=undefined}) {
    const user = useSelector(getUser);
    const client = useURQLClient()

return (
    <Provider value={urqlClient || client}>
        <div className="App"
        className="app-container d-flex flex-column vh-100"
        >
            <NavBar />
            {user.is_login
                ?<DivMap />
                :<LoginForm />
            }
        </div>
    </Provider>
  );
}

export default App;
