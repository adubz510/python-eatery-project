import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import RestaurantList from '../components/RestaurantPage/RestaurantPage';
import Layout from './Layout';
import HomePage from '../components/HomePage/HomePage';
import SearchResultsPage from '../components/RestaurantPage/SearchResultsPage';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "restaurants",
        element: <RestaurantList />,
      },
      {
        path: "search",
        element: <SearchResultsPage />,
      },
    ],
  },
]);