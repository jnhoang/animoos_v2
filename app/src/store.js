import { createStore } from "redux"


// import extensions (thunk)

// import reducers
import reducer from "./reducers/Reducers"


// create store
const store = createStore(reducer);

// export for use
export default store;
