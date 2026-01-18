# MCP Server Configuration

This directory contains the Model Context Protocol (MCP) server configuration for GitHub Copilot.

## Configuration File

- **mcp.json**: Defines which MCP servers are available for Copilot agents and tools in this workspace

## Available MCP Servers

### 1. Serena
- **Purpose**: Semantic code analysis with symbol-level understanding
- **Tools**: Code search, refactoring, cross-project navigation
- **Usage**: Use `#serena` in prompts for code analysis tasks

### 2. Context7
- **Purpose**: Up-to-date documentation and API context
- **Tools**: API documentation lookups, best practices
- **Usage**: Use `#context7` in prompts for documentation lookups
- **Requires**: `CONTEXT7_API_KEY` environment variable

### 3. GitHub
- **Purpose**: Repository operations and GitHub API access
- **Tools**: Issues, PRs, code search, repository operations
- **Requires**: `GITHUB_TOKEN` environment variable

### 4. Filesystem
- **Purpose**: Safe file operations within the workspace
- **Tools**: File read, write, search within project boundaries

## Environment Variables

Set these environment variables for full functionality:

```bash
export CONTEXT7_API_KEY="your-context7-api-key"
export GITHUB_TOKEN="your-github-token"
```

## Best Practices

1. **This file is version controlled** to ensure team consistency
2. **Secrets are not stored here** - use environment variables
3. **Local overrides**: Create `~/.copilot/mcp-config.json` for personal settings
4. **Trust**: Only use MCP servers from trusted sources

## Troubleshooting

If MCP servers don't work:
1. Ensure environment variables are set
2. Check that required tools are installed (`node`, `npx`, `uvx`)
3. Restart VS Code or your IDE
4. Check logs in VS Code: View → Output → GitHub Copilot

## References

- [GitHub Copilot MCP Documentation](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp)
- [Serena MCP Server](https://github.com/oraios/serena)
- [Context7 MCP Server](https://www.npmjs.com/package/@upstash/context7-mcp)
