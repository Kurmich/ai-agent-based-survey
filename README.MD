# Automated Survey Collection Using LLM-Based Conversational Agents  
  
This repository contains the code and data used in a pilot study that explores the use of large language model (LLM)-powered agents to automate survey collection and analysis. The framework for the survey collection process is illustrated in the figure below: 
![framework architecture](https://github.com/Kurmich/ai-agent-based-survey/blob/main/system_architecture.png) 
  
## Framework Overview  
  
The survey collection system integrates several key components:  
  
1. **Researcher**    
   - Designs the survey and writes tailored prompts for large language models.    
  
2. **AI-Based Conversational Phone Agent**    
   - Provided by Bland.ai, this agent conducts phone surveys and stores conversations.    
  
3. **Survey Participant**    
   - Engages in conversation with the AI phone agent to provide answers to survey questions.    
  
4. **Large Language Model (GPT-4o)**    
   - Analyzes participant conversations to deduce answers for individual survey questions.    
  
5. **REDCap Database**    
   - Stores survey results for further use.    
  

---
  
## Example Walkthrough  
  
For an example of how the survey collection and analysis process works, refer to **`survey_demo.ipynb`**. 
This notebook demonstrates step-by-step survey collection  process.  

--- 
 
## Preprocessing and Postprocessing Notebooks  
  
This repository includes the following notebooks for key stages of the study:  
  
- **`data_cleaner.ipynb`**    
  Prepares and transforms the original COVID Impact Survey into an adapted format used in our surveys.    
  
- **`persona_generator.ipynb`**    
  Generates personas that were used by study participants during the experiment.    
  
- **`output_analyzer.ipynb`**    
  Computes the accuracy of survey responses deduced by reasoning LLM (GPT-4o).    
  
