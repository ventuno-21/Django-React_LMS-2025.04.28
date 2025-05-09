import { Route, Routes, BrowserRouter } from "react-router-dom"
import MainWrapper from "./layouts/MainWrapper"
import PrivateRoute from "./layouts/PrvateRoute"



function App() {

  return (
    <>
      <BrowserRouter>
        <MainWrapper>
          <Routes>
            {/* <Route path='/register/' element={<Register />} /> */}
          </Routes>
        </MainWrapper>
      </BrowserRouter>
    </>
  )
}

export default App
