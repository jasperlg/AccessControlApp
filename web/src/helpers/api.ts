import config from '../config/config.json';

const get = async (endpoint: string): Promise<any> => {
    let auth = '';
    if (sessionStorage.getItem('AccessToken') != null && sessionStorage.getItem('AccessToken') != undefined) {
        let auth = sessionStorage.getItem('AccessToken');
    }

    const response: Response = await fetch(
        config.API_URL + endpoint,
        {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Authorization': auth
            }
        });

    if (response.ok) {
        return response.json();
    }
    else {
        // TODO: throw?
        return response.text();
    }
}

const post = async (endpoint: string, data: Object): Promise<any> => {
    let auth = '';
    if (sessionStorage.getItem('AccessToken') != null && sessionStorage.getItem('AccessToken') != undefined) {
        let auth = sessionStorage.getItem('AccessToken');
    }

    const response: Response = await fetch(
        config.API_URL + endpoint,
        {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Authorization': auth,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

    if (response.ok) {
        return response.json();
    }
    else {
        // TODO: throw?
        return response.text();
    }
}

export { get, post };
