import { SyntheticEvent, useState } from "react";

import { FormTextArea, FormButton, Form } from "semantic-ui-react";

type Template = {
    key: string;
    text: string;
    value: string;
};

const templates: Template[] = [
    { key: "1", text: "Template 1", value: "template_001" },
    { key: "2", text: "Template 2", value: "template_002" },
    { key: "3", text: "Template 3", value: "template_003" },
];

function apiSubmitCV(cvContent: string, template_id: string) {
    var backendUrl = `http://127.0.0.1:8000/generate-cv/text?user_id=1&template_id=${template_id}`;
    var data = {
        content: cvContent,
    };
    fetch(backendUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log("Success:", data);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}

function FormExampleSubcomponentControl() {
    const [cvContent, setCvContent] = useState("");
    const [template, setTemplate] = useState("template_001");

    function handleSubmit() {
        apiSubmitCV(cvContent, template);
    }

    return (
        <Form onSubmit={handleSubmit}>
            <FormTextArea
                label="CV Content"
                placeholder="Paste your CV content here"
                rows={10}
                onChange={(e) => setCvContent(e.target.value)}
            />
            <Form.Select
                options={templates}
                defaultValue={"template_001"}
                onChange={(_e: SyntheticEvent<HTMLElement, Event>, { value }) =>
                    setTemplate(value as string)
                }
            />
            <FormButton>Submit</FormButton>
        </Form>
    );
}

export default FormExampleSubcomponentControl;
