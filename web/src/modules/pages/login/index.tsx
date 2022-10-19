import React from 'react';
import styled from 'styled-components';
import config from '../../../config/config.json'
import * as api from '../../../helpers/api';
import Header from '../../common/components/header';

const Center = styled.div`
    display: flex;
    height: 100%;
    width: 100%;

    justify-content: center;
    align-items: center;
`;

const LoginBox = styled.section`
    padding: 2rem;

    border: 1px black solid;
`;

const PageTitle = styled.h2`
    font-size: 2rem;
    text-align: center;

    margin-bottom: 2rem;
`;

const FormInputBox = styled.div`
    display: flex;
    justify-content: space-between;

    margin-bottom: 1rem;
`;

const FormBox = styled.div`
    display: flex;
    justify-content: center;
`

const Button = styled.input`
    text-align: center;
`;

const LoginPage = () => {
    const login = async (e: React.FormEvent) => {
        e.preventDefault();
        
        const response = await api.post('/api/auth/login', {
            'password': password,
            'name': username
        });

        // sessionStorage.setItem('AccessToken', response.Authorization);
        // console.log(sessionStorage.getItem('AccessToken'));

        
        const res2 = await api.get('/api/ticket');
        console.log(res2);
    }

    const [username, setUsername] = React.useState<string>('');
    const [password, setPassword] = React.useState<string>('');

    return (
        <>
        <Header />
        <main>
            <Center>
                <LoginBox>
                    <PageTitle>Login</PageTitle>
                    <form onSubmit={login}>
                        <FormInputBox>
                            <label htmlFor="username">gebruikers naam</label>
                            <input id="username" name="username" type="text" value={username} onChange={(e) => {setUsername(e.target.value)}} />
                        </FormInputBox>
                        <FormInputBox>
                            <label htmlFor="password">wachtwoord</label>
                            <input id="password" name="password" type="password" value={password} onChange={(e) => {setPassword(e.target.value)}} />     
                        </FormInputBox>
                        <FormBox>
                            <Button id="login" name="login" type="submit" value="Login" />
                        </FormBox>
                    </form>
                </LoginBox>
            </Center>
        </main>
        </>
    );
};

export default LoginPage;
