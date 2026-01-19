# System Architecture

## Data Flow Overview

1. User provides a startup idea or market domain
2. Research Agent discovers competitors and collects raw data using web tools
3. Analyst Agent extracts pricing models, customer segments, and patterns
4. Writer Agent produces a structured market report
5. All intermediate and final outputs are persisted for reuse

The system is designed to be repeatable and extendable to support continuous monitoring.

## Agent Contracts

### Research Agent

**Input**
- Market domain or startup idea (string)

**Tools**
- Web search
- Website fetching
- Text extraction

**Output**
```json
{
  "competitors": [
    {
      "name": "string",
      "website": "string",
      "description": "string",
      "source": "url"
    }
  ]
}

### Analyst Agent

**Input**
- Research Agent output

**Responsibilities**
- Identify pricing models
- Group competitors by customer segment
- Detect positioning patterns


**Output**
```json
{
  "pricing_models": ["subscription", "usage-based"],
  "customer_segments": ["SMBs", "enterprises"],
  "competitive_patterns": ["freemium adoption"]
}

### Writer Agent

**Input**
- Analyst Agent output

**Responsibilities**
- Generate structured, human-readable reports
- Do not introduce new facts

**Output**
- Markdown or HTML report
- Tables for comparison

## Tool Usage Principles

- Agents must use tools to obtain external information
- LLMs are not allowed to fabricate facts
- All external data must include source URLs
- Failures should return partial but valid outputs