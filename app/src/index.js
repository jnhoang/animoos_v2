import React      from 'react';
import ReactDOM   from 'react-dom';
import App        from './App';
import registerServiceWorker from './registerServiceWorker';


// redux modules
import { Provider } from 'react-redux'
import store        from './store'


// define react entry point
const entryPoint = document.getElementById('root')
ReactDOM.render(
  <Provider store={ store }>
    <App /> 
  </Provider>,
  entryPoint
);

// for caching
registerServiceWorker();
