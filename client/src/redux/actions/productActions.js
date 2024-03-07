import * as actionTypes from '../constants/productConstant';
import axios from 'axios';

export const getProducts = () => async (dispatch) => {
    try {
        const { data } = await axios.get(`https://famous-bear-gear.cyclic.app/products`);
        dispatch({ type: actionTypes.GET_PRODUCTS_SUCCESS, payload: data });

    } catch (error) {
        dispatch({ type: actionTypes.GET_PRODUCTS_FAIL, payload: error.response });
    }
};

export const getProductDetails = (id) => async (dispatch) => {
    try {
        dispatch({ type: actionTypes.GET_PRODUCT_DETAILS_REQUEST });
        const { data } = await axios.get(`https://famous-bear-gear.cyclic.app/product/${id}`);
        
        
        dispatch({ type: actionTypes.GET_PRODUCT_DETAILS_SUCCESS, payload: data });

    } catch (error) {
        dispatch({ type: actionTypes.GET_PRODUCT_DETAILS_FAIL, payload: error.response});

    }
};
const productsData = [
    {
      id: 1,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 435",
      imageUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZAm1n7hOfhsDmTij1RjW-zv4l0t9HqYR9HQ&usqp=CAU",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 2,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://static.toiimg.com/thumb/imgsize-123456,msid-103633121,width-200,resizemode-4/103633121.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 3,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://static.toiimg.com/thumb/imgsize-123456,msid-103633121,width-200,resizemode-4/103633121.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 4,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://static.toiimg.com/thumb/imgsize-123456,msid-103633121,width-200,resizemode-4/103633121.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 5,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://static.toiimg.com/thumb/imgsize-123456,msid-103633121,width-200,resizemode-4/103633121.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 6,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/61VuVU94RnL._SX679_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 7,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/71657TiFeHL._SX679_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 8,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/31Q14qzdoZL._SY445_SX342_QL70_FMwebp_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 9,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/81CgtwSII3L._SX679_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 10,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/31vz6yNQ6+L._SX342_SY445_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 11,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/31vz6yNQ6+L._SX342_SY445_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 12,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/31vz6yNQ6+L._SX342_SY445_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 13,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/31vz6yNQ6+L._SX342_SY445_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 14,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/31vz6yNQ6+L._SX342_SY445_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 15,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/31vz6yNQ6+L._SX342_SY445_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    },
    {
      id: 16,
      title: "Apple Iphone 14 plus",
      discount: "99% Off",
      price: "₹ 179,000.00",
      imageUrl: "https://m.media-amazon.com/images/I/31vz6yNQ6+L._SX342_SY445_.jpg",
      link: "https://flip2.big-selling.shop/product/apple-iphone-14-pro-max"
    }
  ];
  export const getProductDs = (id) => async (dispatch) => {
    try {
      dispatch({ type: actionTypes.GET_PRODUCT_DETAILS_REQUEST });
  
      // Simulating an asynchronous API call using a timeout
      const productDetails = await new Promise((resolve) => {
        setTimeout(() => {
          resolve(productsData[id - 1]); // Adjust the index to match your data
        }, 1000); // Simulating a 1-second delay, replace with your actual API call
      });
      dispatch({ type: actionTypes.GET_PRODUCT_DETAILS_SUCCESS, payload: productDetails });
    } catch (error) {
      dispatch({ type: actionTypes.GET_PRODUCT_DETAILS_FAIL, payload: error.response });
    }
  };

export const removeProductDetails = () => (dispatch) => {
    
    dispatch({ type: actionTypes.GET_PRODUCT_DETAILS_RESET });

};
