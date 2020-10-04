## introduction path
* greet
  - utter_tell_capablity
  - utter_ask_fname
* fname{"fname":"akash"}
  - utter_ask_lname
* lname{"lname":"bhandari"}
  - utter_ask_age
* age_sal{"age":"24"}
  - utter_ask_location
  - action_database_update
* location {"location":"mumbai"}
  - utter_ask_are_you_here_after_surgery
> Check_details

## afirm path
> Check_details
* affirm

## deny path
> Check_details
* deny
- utter_ask_problem

## fever path
* fever
- utter_ask_how_long_have_you_fever
* fever_less_than_week
- utter_ask_how_high_does_the_fever_go
* fever_temp
- utter_ask_do_you_have_any_of_these_respitory_problem

## cough fever path
* cough
- utter_ask_do_you_have_any_of_these_problem_as_well_flu
- action_show_symptom_of_flu_basis_of_age
> flu_conform

## affirm path flu
> flu_conform
* affirm
- action_disease_flu_conform
- action_feedback_submit
* feedback {"feedback": "Love to chat with you healthbot"}
- action_feedback_database

## flu_cough
> flu_conform
* flu_cough
- action_disease_flu_conform
- action_feedback_submit
* feedback {"feedback": "Love to chat with you healthbot"}
- action_feedback_database

## deny
> flu_conform
* deny
- utter_ask_do_you_have_any_of_these_problem_as_well_laryngitis
- action_show_symptom_of_laryngitis_basis_of_age
> laryngitis_conform

## affirm path laryngitis
> laryngitis_conform
* affirm
- action_disease_laryngitis_conform
- action_feedback_submit
* feedback {"feedback": "Love to chat with you healthbot"}
- action_feedback_database

## laryngitis_cough
> laryngitis_conform
* laryngitis_cough
- action_disease_laryngitis_conform
- action_feedback_submit
* feedback {"feedback": "Love to chat with you healthbot"}
- action_feedback_database

## deny
> laryngitis_conform
* deny
- utter_ask_do_you_have_any_of_these_problem_as_well_laryngitis
- action_show_symptom_of_laryngitis_basis_of_age





























## severe body ache path
* severe_body_ache
- utter_ask_do_you_have_any_of_these_problem_as_well_body_ache
* severe_body_ache_conform
- action_disease_fever_dengu

## headache fever path
* headache
- utter_ask_do_you_have_any_of_these_problem_as_well_headache
* headache_conform
- action_disease_fever_meningitis

## sore throat path
* sore_throat
- utter_ask_do_you_have_any_of_these_problem_as_well_sore_throat
* sore_throat_conform
- action_disease_fever_pharyngitis
