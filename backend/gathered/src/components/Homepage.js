import React, { Component } from "react";
import { Card, Button, Navbar, Nav  } from "react-bootstrap";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    renderCard = () => {
        return (
            <Card style={{ width:'18rem' }}>
                <Card.Header>Featured</Card.Header>
                <Card.Body>
                    <Card.Title>testing</Card.Title>
                    <Card.Text>
                        testing
                    </Card.Text>
                    <Button variant="primary">testing</Button>
                </Card.Body>
            </Card>
        );
    }

    render() {
        return (
            <div>
                { this.renderCard() }
            </div>
        )
    }
}