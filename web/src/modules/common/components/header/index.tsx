import React from 'react';
import logo from './logo.jpg';
import styled from 'styled-components';

const HeaderComponent = styled.header`
    height: 4rem;
    padding: 1rem;
    margin-bottom: 4rem;

    display: flex;
    align-items: center;
`;

const Logo = styled.img`
    height: 100%;

    margin-right: 4rem;
`;

const Title = styled.h1`
    font-size: 2rem;

    display: inline-block;
`;

const Header = () => (
    <HeaderComponent>
        <Logo src={logo} alt="logo" />
        <Title>Access Control App</Title>
    </HeaderComponent>
);

export default Header;
