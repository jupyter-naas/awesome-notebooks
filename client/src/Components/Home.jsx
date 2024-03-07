import React,  { useEffect } from 'react';

import { Box, styled } from '@mui/material';
// import ProductCard from './Home/ProductCard';
import NavBar from './Home/NarBar';
import Banner from './Home/Banner';
import MidSlide from './Home/MidSlide';
import MidSection from './Home/MidSection';
import Slide from './Home/Slide';
import ProductCard from './Home/ProductCard';
import { useSelector, useDispatch } from 'react-redux'; // hooks
import { getProducts as listProducts } from '../redux/actions/productActions';
import Countdown from 'react-countdown';

const Component = styled(Box)`
    padding: 20px 10px;
    background: #F2F2F2;
`;
const Componenta = styled('p')({
  marginTop: 30,
  padding: '15px 20px',
  textAlign: 'center',
  fontWeight: 'bold',
});

const Home = () => {
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
      
      // Now you can use the 'productsData' array as your data field in your application.
      
    const getProducts = useSelector(state => state.getProducts);
    const AllBox = styled(Box)({
      textAlign: 'center',
      padding: 10,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    });
    
    const TimerImage = styled('img')({
      marginBottom: 10,
    });
    const timerURL = 'https://static-assets-web.flixcart.com/www/linchpin/fk-cp-zion/img/timer_a73398.svg';
    const renderer = ({ hours, minutes, seconds, completed }) => {
          return <span>{minutes}:{seconds} left</span>;
      };
    const { products, error } = getProducts;

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(listProducts())
    }, [dispatch])
      return (
        <>
            <NavBar />
            <Component>
                <Banner />
                <MidSlide products={products} />
                <MidSection />
                {/* <Slide
                    data={products} 
                    title='Discounts for You'
                    timer={false} 
                    multi={true} 
                /> */}

            </Component>
            <Box>
        <Componenta>Deal of the Day </Componenta>
        <AllBox>
          <TimerImage src={timerURL} alt="timer" />
          <Countdown date={Date.now()+5.04e+7 } renderer={renderer}/>
        </AllBox>
        </Box>
        <div className="product-list">
            {products.map(product => (
            <ProductCard key={product._id} {...product} />
            ))}
        </div>
        </>
    )
}

export default Home;