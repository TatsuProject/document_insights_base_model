def get_document_prompt(document_type: str, context: str) -> str:
    letter_prompt = """
        This is a letter, and your job is to parse this document into a dictionary. 
        Letter content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "sender_name": {{"text": "", "bounding_box": []}},
            "sender_address": {{"text": "", "bounding_box": []}},
            "sender_contact": {{"text": "", "bounding_box": []}},
            "date": {{"text": "", "bounding_box": []}},
            "receiver_name": {{"text": "", "bounding_box": []}},
            "receiver_address": {{"text": "", "bounding_box": []}},
            "attachments": [{{"text": "", "bounding_box": []}}]
        }}
    """


    memo_prompt = """
        This is a memo, and your job is to parse this document into a dictionary. 
        Memo content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "sender_name": {{"text": "", "bounding_box": []}},
            "sender_position": {{"text": "", "bounding_box": []}},
            "recipient_name": {{"text": "", "bounding_box": []}},
            "recipient_position": {{"text": "", "bounding_box": []}},
            "cc": [{{"text": "", "bounding_box": []}}],
            "date": {{"text": "", "bounding_box": []}},
            "subject": {{"text": "", "bounding_box": []}},
            "reference_number": {{"text": "", "bounding_box": []}},
            "attachments": [{{"text": "", "bounding_box": []}}]
        }}    
    """



    email_prompt = """
        This is an email, and your job is to parse this document into a dictionary. 
        Email content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "sender_name": {{"text": "", "bounding_box": []}},
            "sender_email": {{"text": "", "bounding_box": []}},
            "recipient_name": {{"text": "", "bounding_box": []}},
            "recipient_email": {{"text": "", "bounding_box": []}},
            "cc": [{{"text": "", "bounding_box": []}}],
            "bcc": [{{"text": "", "bounding_box": []}}],
            "date": {{"text": "", "bounding_box": []}},
            "time": {{"text": "", "bounding_box": []}},
            "subject": {{"text": "", "bounding_box": []}},
            "signature": {{"text": "", "bounding_box": []}},
            "attachments": [{{"text": "", "bounding_box": []}}],
        }}    
    """



    form_prompt = """
        This is a form, and your job is to parse this document into a dictionary. 
        Form content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "form_title": {{"text": "", "bounding_box": []}},
            "applicant_details": {{
                "full_name": {{"text": "", "bounding_box": []}},
                "date_of_birth": {{"text": "", "bounding_box": []}},
                "gender": {{"text": "", "bounding_box": []}},
                "nationality": {{"text": "", "bounding_box": []}}
            }},
            "contact_information": {{
                "phone_number": {{"text": "", "bounding_box": []}},
                "email_address": {{"text": "", "bounding_box": []}},
                "home_address": {{"text": "", "bounding_box": []}}
            }},
            "identification_details": {{
                "id_number": {{"text": "", "bounding_box": []}},
                "social_security_number": {{"text": "", "bounding_box": []}}
            }},
            "employment_details": {{
                "company_name": {{"text": "", "bounding_box": []}},
                "job_title": {{"text": "", "bounding_box": []}},
                "work_address": {{"text": "", "bounding_box": []}}
            }},
            "financial_details": {{
                "account_number": {{"text": "", "bounding_box": []}},
                "taxpayer_id": {{"text": "", "bounding_box": []}},
                "salary_information": {{"text": "", "bounding_box": []}}
            }},
            "submission_date": {{"text": "", "bounding_box": []}},
            "reference_number": {{"text": "", "bounding_box": []}}
        }}    
    """


    invoice_prompt = """
        This is an Invoice, and your job is to parse this document into a dictionary. 
        Invoice content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "organization": {{"text": "", "bounding_box": []}},
            "date": {{"text": "", "bounding_box": []}},
            "invoice_number": {{"text": "", "bounding_box": []}},
            "payee_name": {{"text": "", "bounding_box": []}},
            "purchased_item": [
                {{ "item": {{"text": "", "bounding_box": []}},
                "price": {{"text": "", "bounding_box": []}}
                }},
                {{ "item": {{"text": "", "bounding_box": []}},
                "price": {{"text": "", "bounding_box": []}}
                }}
            ],
            "total_amount": {{"text": "", "bounding_box": []}},
            "discount_amount": {{"text": "", "bounding_box": []}},
            "tax_amount": {{"text": "", "bounding_box": []}},
            "final_amount": {{"text": "", "bounding_box": []}}
        }}
    """


        
    handwritten_prompt = """
        This is a general document, and your job is to parse this document into a dictionary. 
        document content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "person_names": [{{"text": "", "bounding_box": []}}],
            "dates": [{{"text": "", "bounding_box": []}}]
        }}
    """


    advertisement_prompt = """
        This is an advertisement document, and your job is to parse this document into a dictionary. 
        The advertisement content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "advertisement_title": {{"text": "", "bounding_box": []}},
            "advertiser_information": {{
                "company_name": {{"text": "", "bounding_box": []}},
                "contact_information": {{
                    "phone": {{"text": "", "bounding_box": []}},
                    "email": {{"text": "", "bounding_box": []}},
                    "website": {{"text": "", "bounding_box": []}}
                }}
            }},
            "product_service_details": {{
                "product_service_name": {{"text": "", "bounding_box": []}},
                "description": {{"text": "", "bounding_box": []}},
                "features_benefits": {{"text": "", "bounding_box": []}},
                "pricing": {{"text": "", "bounding_box": []}}
            }},
            "promotional_offers": {{"text": "", "bounding_box": []}},
            "call_to_action": {{"text": "", "bounding_box": []}},
            "advertisement_date": {{"text": "", "bounding_box": []}},
            "location_information": {{"text": "", "bounding_box": []}},
            "social_media_links": [{{"text": "", "bounding_box": []}}],
            "legal_disclaimers": {{"text": "", "bounding_box": []}}
        }}    
    """


    scientific_publication_prompt = """
        This is a scientific publication, and your job is to parse this document into a structured dictionary.
        The publication content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "title": {{"text": "", "bounding_box": []}},
            "authors": [
                {{
                    "name": {{"text": "", "bounding_box": []}},
                    "affiliation": {{"text": "", "bounding_box": []}}
                }}
            ],
            "abstract": {{"text": "", "bounding_box": []}},
            "publication_date": {{"text": "", "bounding_box": []}},
            "journal_conference_name": {{"text": "", "bounding_box": []}}
        }}    
    """


    presentation_prompt = """
        This is a presentation slide, and your job is to parse this document into a structured dictionary.
        The slide content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "slide_title": {{"text": "", "bounding_box": []}}
        }}    
    """


    news_article_prompt = """
        This is a news article, and your job is to parse this document into a structured dictionary.
        The article content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "headline": {{"text": "", "bounding_box": []}},
            "date": {{"text": "", "bounding_box": []}},
            "author": {{"text": "", "bounding_box": []}},
            "category": {{"text": "", "bounding_box": []}},
            "source": {{"text": "", "bounding_box": []}}
        }}    
    """


    budget_prompt = """
        This is a budget document, and your job is to parse this document into a structured dictionary.
        The budget details are given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "budget_name": {{"text": "", "bounding_box": []}},
            "date": {{"text": "", "bounding_box": []}},
            "total_budget": {{"text": "", "bounding_box": []}},
            "currency": {{"text": "", "bounding_box": []}},
            "allocations": [
                {{
                    "category": {{"text": "", "bounding_box": []}},
                    "amount": {{"text": "", "bounding_box": []}}
                }},
                {{
                    "category": {{"text": "", "bounding_box": []}},
                    "amount": {{"text": "", "bounding_box": []}}
                }}
            ]
        }}    
    """


    resume_prompt = """
        This is a resume, and your job is to parse this document into a structured dictionary.
        The resume content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "name": {{"text": "", "bounding_box": []}},
            "contact_info": {{
                "email": {{"text": "", "bounding_box": []}},
                "phone": {{"text": "", "bounding_box": []}},
                "address": {{"text": "", "bounding_box": []}}
            }},
            "skills": [
                {{"text": "", "bounding_box": []}},
                {{"text": "", "bounding_box": []}}
            ],
            "education": [
                {{
                    "degree": {{"text": "", "bounding_box": []}},
                    "institution": {{"text": "", "bounding_box": []}},
                    "year": {{"text": "", "bounding_box": []}}
                }}
            ],
            "work_experience": [
                {{
                    "job_title": {{"text": "", "bounding_box": []}},
                    "company": {{"text": "", "bounding_box": []}},
                    "years": {{"text": "", "bounding_box": []}}
                }}
            ]
        }}    
    """


    questionnaire_prompt = """
        This is a questionnaire, and your job is to parse this document into a structured dictionary.
        The questionnaire content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "title": {{"text": "", "bounding_box": []}},
            "date": {{"text": "", "bounding_box": []}},
            "respondent_name": {{"text": "", "bounding_box": []}},
            "respondent_id": {{"text": "", "bounding_box": []}}
        }}
    """


    scientific_report_prompt = """
        This is a scientific report, and your job is to parse this document into a structured dictionary.
        The report content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "title": {{"text": "", "bounding_box": []}},
            "authors": [
                {{
                    "name": {{"text": "", "bounding_box": []}},
                    "affiliation": {{"text": "", "bounding_box": []}}
                }}
            ],
            "date": {{"text": "", "bounding_box": []}},
            "keywords": [
                {{"text": "", "bounding_box": []}},
                {{"text": "", "bounding_box": []}}
            ],
            "report_id": {{"text": "", "bounding_box": []}},
            "funding_source": {{"text": "", "bounding_box": []}}
        }}    
    """


    file_folder_prompt = """
        This is a file folder document, and your job is to parse this document into a structured dictionary.
        The document content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "folder_title": {{"text": "", "bounding_box": []}},
            "folder_id": {{"text": "", "bounding_box": []}},
            "creation_date": {{"text": "", "bounding_box": []}},
            "owner": {{"text": "", "bounding_box": []}},
            "department": {{"text": "", "bounding_box": []}},
            "contained_documents": [
                {{
                    "document_title": {{"text": "", "bounding_box": []}},
                    "document_id": {{"text": "", "bounding_box": []}},
                    "date_added": {{"text": "", "bounding_box": []}}
                }}
            ],
            "tags": [
                {{"text": "", "bounding_box": []}}
            ]
        }}    
    """


    specifications_prompt = """
        This is a specification document, and your job is to parse this document into a structured dictionary.
        The document content is given below, delimited by three hashes.

        ###
        {context}
        ###

        Just fill the following template and return it in dictionary format. Keep "bounding_box" as an empty list. Only generate a dictionary in your response, nothing else.

        {{
            "title": {{"text": "", "bounding_box": []}},
            "date": {{"text": "", "bounding_box": []}},
            "organization": {{"text": "", "bounding_box": []}},
            "key_sections": [
                {{
                    "section_title": {{"text": "", "bounding_box": []}},
                    "section_number": {{"text": "", "bounding_box": []}}
                }}
            ],
            "regulatory_compliance": [
                {{"text": "", "bounding_box": []}}
            ],
            "key_requirements": [
                {{"text": "", "bounding_box": []}}
            ]
        }}    
    """


    if document_type == "letter":
        return letter_prompt.format(context=context)
    elif document_type == "memo":
        return memo_prompt.format(context=context)
    elif document_type == "email":
        return email_prompt.format(context=context)
    elif document_type == "form":
        return form_prompt.format(context=context)
    elif document_type == "invoice":
        return invoice_prompt.format(context=context)
    elif document_type == "handwritten":
        return handwritten_prompt.format(context=context)
    elif document_type == "advertisement":
        return advertisement_prompt.format(context=context)
    elif document_type == "scientific_publication":
        return scientific_publication_prompt.format(context=context)
    elif document_type == "presentation":
        return presentation_prompt.format(context=context)
    elif document_type == "news_article":
        return news_article_prompt.format(context=context)
    elif document_type == "budget":
        return budget_prompt.format(context=context)
    elif document_type == "resume":
        return resume_prompt.format(context=context)
    elif document_type == "questionnaire":
        return questionnaire_prompt.format(context=context)
    elif document_type == "scientific_report":
        return scientific_report_prompt.format(context=context)
    elif document_type == "file_folder":
        return file_folder_prompt.format(context=context)
    elif document_type == "specification":
        return specifications_prompt.format(context=context)
    else:
        return "Invalid document type"

